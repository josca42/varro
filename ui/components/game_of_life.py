from __future__ import annotations

from fasthtml.common import Div, Canvas, Script


def GameOfLifeAnimation(size: int = 40, cell_size: int = 2, run: bool = False):
    return Div(
        Canvas(
            cls="gol-canvas",
            **{
                "data-gol": "1",
                "data-size": str(size),
                "data-cell": str(cell_size),
                "data-run": "1" if run else "0",
                "width": str(size),
                "height": str(size),
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

  const state = new WeakMap();

  const initCanvas = (canvas) => {
    if (!canvas || state.has(canvas)) return state.get(canvas);
    const size = parseInt(canvas.dataset.size || "40", 10);
    const cellSize = parseInt(canvas.dataset.cell || "2", 10);
    canvas.width = size;
    canvas.height = size;

    const ctx = canvas.getContext("2d");
    if (!ctx) return null;

    const cols = Math.max(1, Math.floor(size / cellSize));
    const rows = Math.max(1, Math.floor(size / cellSize));
    const color = "#9b2743";

    let grid = [];
    let targetGrid = [];
    let finalGrid = [];
    let isAnimating = false;
    let animationId = null;
    let lastTime = 0;
    const interval = 80;

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

    const isNearTarget = (x, y) => {
      for (let i = -2; i <= 2; i++) {
        for (let j = -2; j <= 2; j++) {
          const nx = x + i;
          const ny = y + j;
          if (nx >= 0 && nx < cols && ny >= 0 && ny < rows) {
            if (targetGrid[nx][ny] === 1) return true;
          }
        }
      }
      return false;
    };

    const createFinalGrid = () => {
      finalGrid = Array.from({ length: cols }, () => Array(rows).fill(0));
      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          if (targetGrid[x][y] === 1) {
            const noise = Math.sin(x * 0.7 + y * 0.5) * Math.cos(x * 0.3 - y * 0.8);
            finalGrid[x][y] = noise > 0.7 && Math.random() > 0.5 ? 0 : 1;
          } else {
            const nearV = isNearTarget(x, y);
            finalGrid[x][y] = nearV && Math.random() > 0.92 ? 1 : 0;
          }
        }
      }
    };

    const initGrid = () => {
      grid = Array.from({ length: cols }, () => Array(rows).fill(0));
      const margin = cols * 0.15;
      const left = margin;
      const right = cols - margin;
      const top = margin;
      const bottom = rows - margin;

      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          const inSquare = x >= left && x <= right && y >= top && y <= bottom;
          if (!inSquare) continue;

          const distToLeft = x - left;
          const distToRight = right - x;
          const distToTop = y - top;
          const distToBottom = bottom - y;
          const distToEdge = Math.min(distToLeft, distToRight, distToTop, distToBottom);
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

    const setFinalState = () => {
      if (!grid.length) {
        grid = Array.from({ length: cols }, () => Array(rows).fill(0));
      }
      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          grid[x][y] = finalGrid[x][y];
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

    const step = () => {
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

          if (isTarget) {
            if (newState === 0 && Math.random() < 0.04) newState = 1;
            if (newState === 0 && alive && Math.random() < 0.18) newState = 1;
          } else if (newState === 1 && Math.random() < 0.05) {
            newState = 0;
          }

          newGrid[x][y] = newState;
        }
      }
      grid = newGrid;
    };

    const draw = () => {
      ctx.clearRect(0, 0, size, size);
      for (let x = 0; x < cols; x++) {
        for (let y = 0; y < rows; y++) {
          if (grid[x][y] === 1) {
            ctx.fillStyle = color;
            ctx.fillRect(x * cellSize, y * cellSize, cellSize - 1, cellSize - 1);
          }
        }
      }
    };

    const animate = (time) => {
      if (!isAnimating) return;
      if (!canvas.isConnected) return;
      if (time - lastTime > interval) {
        step();
        draw();
        lastTime = time;
      }
      animationId = requestAnimationFrame(animate);
    };

    const startLoading = () => {
      if (isAnimating) return;
      isAnimating = true;
      initGrid();
      draw();
      lastTime = 0;
      animationId = requestAnimationFrame(animate);
    };

    const stopLoading = () => {
      isAnimating = false;
      if (animationId) cancelAnimationFrame(animationId);
      setFinalState();
      draw();
    };

    createVTarget();
    createFinalGrid();
    setFinalState();
    draw();

    const api = { startLoading, stopLoading };
    state.set(canvas, api);
    return api;
  };

  window.__golRefresh = () => {
    document.querySelectorAll("canvas[data-gol]").forEach((canvas) => {
      const api = initCanvas(canvas);
      if (!api) return;
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
