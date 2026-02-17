from __future__ import annotations

from fasthtml.common import Div, Canvas, Script


def GameOfLifeAnimation(
    size: int = 40,
    cell_size: int = 2,
    run: bool = False,
    *,
    width: int | None = None,
    height: int | None = None,
    text: str = "",
    color: str = "",
    autoplay: int = 0,
    cls: str = "",
):
    w = width or size
    h = height or size
    return Div(
        Canvas(
            cls=f"gol-canvas {cls}".strip(),
            **{
                "data-gol": "1",
                "data-size": str(size),
                "data-width": str(w),
                "data-height": str(h),
                "data-cell": str(cell_size),
                "data-run": "1" if run else "0",
                "data-text": text,
                "data-color": color,
                "data-autoplay": str(autoplay),
                "width": str(w),
                "height": str(h),
            },
        ),
        Script(_game_of_life_script()),
        cls="gol-animation",
    )


def _game_of_life_script() -> str:
    return """
(() => {
  if (window.__golRefresh) {
    window.__golRefresh();
    return;
  }

  const PIXEL_FONT = {
    V: [
      "10001",
      "10001",
      "10001",
      "01010",
      "01010",
      "01010",
      "00100",
    ],
    A: [
      "01110",
      "10001",
      "10001",
      "11111",
      "10001",
      "10001",
      "10001",
    ],
    R: [
      "11110",
      "10001",
      "10001",
      "11110",
      "10010",
      "10001",
      "10001",
    ],
    O: [
      "01110",
      "10001",
      "10001",
      "10001",
      "10001",
      "10001",
      "01110",
    ],
  };

  const state = new WeakMap();

  const initCanvas = (canvas) => {
    if (!canvas || state.has(canvas)) return state.get(canvas);
    const w = parseInt(canvas.dataset.width || canvas.dataset.size || "40", 10);
    const h = parseInt(canvas.dataset.height || canvas.dataset.size || "40", 10);
    const cellSize = parseInt(canvas.dataset.cell || "2", 10);
    const text = canvas.dataset.text || "";
    const autoplaySteps = parseInt(canvas.dataset.autoplay || "0", 10);
    canvas.width = w;
    canvas.height = h;

    const ctx = canvas.getContext("2d");
    if (!ctx) return null;

    const cols = Math.max(1, Math.floor(w / cellSize));
    const rows = Math.max(1, Math.floor(h / cellSize));
    const color = canvas.dataset.color || "#9b2743";

    let grid = [];
    let targetGrid = [];
    let isAnimating = false;
    let animationId = null;
    let lastTime = 0;
    let loadingSteps = 0;
    const interval = 80;

    const createTextTarget = (str) => {
      targetGrid = Array.from({ length: cols }, () => Array(rows).fill(0));
      const chars = str.toUpperCase().split("");
      const glyphs = chars.map(c => PIXEL_FONT[c]).filter(Boolean);
      if (!glyphs.length) return false;

      const charW = 5, charH = 7;
      const gap = 1;
      const totalCharW = glyphs.length * charW + (glyphs.length - 1) * gap;

      const scaleX = Math.floor((cols * 0.8) / totalCharW);
      const scaleY = Math.floor((rows * 0.8) / charH);
      const scale = Math.max(1, Math.min(scaleX, scaleY));

      const scaledW = totalCharW * scale;
      const scaledH = charH * scale;
      const offsetX = Math.floor((cols - scaledW) / 2);
      const offsetY = Math.floor((rows - scaledH) / 2);

      for (let gi = 0; gi < glyphs.length; gi++) {
        const glyph = glyphs[gi];
        const gx = offsetX + gi * (charW + gap) * scale;
        for (let cy = 0; cy < charH; cy++) {
          for (let cx = 0; cx < charW; cx++) {
            if (glyph[cy][cx] === "1") {
              for (let sy = 0; sy < scale; sy++) {
                for (let sx = 0; sx < scale; sx++) {
                  const px = gx + cx * scale + sx;
                  const py = offsetY + cy * scale + sy;
                  if (px >= 0 && px < cols && py >= 0 && py < rows) {
                    targetGrid[px][py] = 1;
                  }
                }
              }
            }
          }
        }
      }
      return true;
    };

    const createVTarget = () => {
      targetGrid = Array.from({ length: cols }, () => Array(rows).fill(0));
      const centerX = cols / 2;
      const startY = Math.floor(rows * 0.1);
      const endY = Math.floor(rows * 0.9);
      const strokeWidth = 2;

      for (let y = startY; y <= endY; y++) {
        const progress = (y - startY) / (endY - startY);
        const spread = (1 - progress) * (cols * 0.4);

        for (let w = -strokeWidth; w <= strokeWidth; w++) {
          const xL = Math.round(centerX - spread + w);
          const xR = Math.round(centerX + spread + w);
          if (xL >= 0 && xL < cols) targetGrid[xL][y] = 1;
          if (xR >= 0 && xR < cols) targetGrid[xR][y] = 1;
        }
      }
    };

    const initGrid = () => {
      grid = Array.from({ length: cols }, () => Array(rows).fill(0));
      const marginX = cols * 0.08;
      const marginY = rows * 0.08;
      const left = marginX, right = cols - marginX;
      const top = marginY, bottom = rows - marginY;

      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          const inRect = x >= left && x <= right && y >= top && y <= bottom;
          if (!inRect) continue;

          const distToEdge = Math.min(x - left, right - x, y - top, bottom - y);
          const edgeFactor = Math.min(distToEdge / 6, 1);
          const noise =
            Math.sin(x * 0.4 + y * 0.3) * 0.4 +
            Math.sin(x * 0.8 - y * 0.6) * 0.3 +
            Math.sin(x * 0.2 + y * 0.9) * 0.3;
          const threshold = 0.35 + (1 - edgeFactor) * 0.35 + noise * 0.15;
          if (Math.random() > threshold) grid[x][y] = 1;
        }
      }
    };

    const countNeighbors = (x, y) => {
      let count = 0;
      for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
          if (i === 0 && j === 0) continue;
          const nx = (x + i + cols) % cols;
          const ny = (y + j + rows) % rows;
          count += grid[nx][ny];
        }
      }
      return count;
    };

    const step = (bias = 1, noise = 0) => {
      const newGrid = Array.from({ length: cols }, () => Array(rows).fill(0));
      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          const neighbors = countNeighbors(x, y);
          const isTarget = targetGrid[x][y] === 1;
          const alive = grid[x][y] === 1;
          let newState = 0;

          if (alive) {
            newState = neighbors === 2 || neighbors === 3 ? 1 : 0;
          } else {
            newState = neighbors === 3 ? 1 : 0;
          }

          if (bias > 0) {
            if (isTarget) {
              if (newState === 0 && Math.random() < 0.08 * bias) newState = 1;
              if (newState === 0 && alive && Math.random() < 0.35 * bias) newState = 1;
            } else if (newState === 1 && Math.random() < 0.12 * bias) {
              newState = 0;
            }
          }

          if (noise > 0 && newState === 0 && Math.random() < noise) {
            newState = 1;
          }

          newGrid[x][y] = newState;
        }
      }
      grid = newGrid;
    };

    const draw = () => {
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = color;
      const size = Math.max(cellSize - 1, 1);
      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          if (grid[x][y] === 1) {
            ctx.fillRect(x * cellSize, y * cellSize, size, size);
          }
        }
      }
    };

    const animate = (time) => {
      if (!isAnimating) return;
      if (!canvas.isConnected) return;
      if (time - lastTime > interval) {
        loadingSteps++;
        const progress = Math.min(loadingSteps / 100, 1);
        const bias = progress < 0.8
          ? Math.min(1, progress * 1.8)
          : 1 + (progress - 0.8) * 4;
        step(bias, 0);
        draw();
        lastTime = time;
      }
      animationId = requestAnimationFrame(animate);
    };

    const startLoading = () => {
      if (isAnimating) return;
      isAnimating = true;
      loadingSteps = 0;
      initGrid();
      draw();
      lastTime = 0;
      animationId = requestAnimationFrame(animate);
    };

    const stopLoading = () => {
      const wasAnimating = isAnimating;
      isAnimating = false;
      if (animationId) cancelAnimationFrame(animationId);
      if (wasAnimating) {
        for (let i = 0; i < 30; i++) step(3, 0);
      }
      draw();
    };

    const runAutoplay = (totalSteps) => {
      if (isAnimating) return;
      isAnimating = true;
      initGrid();
      draw();
      let stepCount = 0;
      lastTime = 0;
      const autoAnimate = (time) => {
        if (!canvas.isConnected) { isAnimating = false; return; }
        if (time - lastTime > interval) {
          const progress = stepCount / totalSteps;
          const bias = progress < 0.8
            ? Math.min(1, progress * 1.8)
            : 1 + (progress - 0.8) * 4;
          step(bias, 0);
          draw();
          lastTime = time;
          stepCount++;
          if (stepCount >= totalSteps) {
            isAnimating = false;
            return;
          }
        }
        animationId = requestAnimationFrame(autoAnimate);
      };
      animationId = requestAnimationFrame(autoAnimate);
    };

    if (text) {
      createTextTarget(text) || createVTarget();
    } else {
      createVTarget();
    }
    if (autoplaySteps > 0) {
      runAutoplay(autoplaySteps);
    } else {
      initGrid();
      for (let i = 0; i < 70; i++) {
        const progress = i / 100;
        const bias = progress < 0.8
          ? Math.min(1, progress * 1.8)
          : 1 + (progress - 0.8) * 4;
        step(bias, 0);
      }
      draw();
    }

    const api = { startLoading, stopLoading };
    state.set(canvas, api);
    return api;
  };

  window.__golRefresh = () => {
    document.querySelectorAll("canvas[data-gol]").forEach((canvas) => {
      const api = initCanvas(canvas);
      if (!api) return;
      const autoplay = parseInt(canvas.dataset.autoplay || "0", 10);
      if (autoplay > 0) return;
      const shouldRun = canvas.dataset.run === "1";
      if (shouldRun) {
        api.startLoading();
      } else {
        api.stopLoading();
      }
    });
  };

  window.__golRefresh();
})();
"""
