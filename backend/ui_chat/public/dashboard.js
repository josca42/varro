// Custom JavaScript for Varro dashboard integration
// This script detects dashboard port markers and forwards to parent window

(function() {
  const MARKER_PATTERN = /<!--DASHBOARD_PORT:(\d+)-->/;
  let lastPort = null;

  function checkForPortMarker(node) {
    if (!node || !node.textContent) return;

    const match = node.textContent.match(MARKER_PATTERN);
    if (match && match[1]) {
      const port = parseInt(match[1], 10);
      if (port && port !== lastPort && window.parent !== window) {
        lastPort = port;
        window.parent.postMessage({ type: 'DASHBOARD_PORT', port: port }, '*');
        console.log('[Varro] Dashboard port sent to parent:', port);
      }
    }
  }

  // Observe DOM for new message content
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      // Check added nodes
      mutation.addedNodes.forEach(function(node) {
        if (node.nodeType === 1) {
          checkForPortMarker(node);
          // Also check child elements
          if (node.querySelectorAll) {
            node.querySelectorAll('*').forEach(checkForPortMarker);
          }
        } else if (node.nodeType === 3) {
          // Text node
          checkForPortMarker(node.parentElement);
        }
      });

      // Check if text content changed
      if (mutation.type === 'characterData') {
        checkForPortMarker(mutation.target.parentElement);
      }
    });
  });

  // Start observing when DOM is ready
  function startObserving() {
    observer.observe(document.body, {
      childList: true,
      subtree: true,
      characterData: true
    });

    // Also check existing content
    document.querySelectorAll('*').forEach(checkForPortMarker);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startObserving);
  } else {
    startObserving();
  }
})();
