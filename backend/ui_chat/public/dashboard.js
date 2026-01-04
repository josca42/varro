// Custom JavaScript for Varro dashboard integration
// This script detects dashboard markers and forwards host+port to parent window

(function() {
  const MARKER_PATTERN = /<!--DASHBOARD:([^:]+):(\d+)-->/;
  let lastKey = null;

  function checkForDashboardMarker(node) {
    if (!node || !node.textContent) return;

    const match = node.textContent.match(MARKER_PATTERN);
    if (match && match[1] && match[2]) {
      const host = match[1];
      const port = parseInt(match[2], 10);
      const key = `${host}:${port}`;
      if (port && key !== lastKey && window.parent !== window) {
        lastKey = key;
        window.parent.postMessage({ type: 'DASHBOARD_PORT', host: host, port: port }, '*');
        console.log('[Varro] Dashboard sent to parent:', host, port);
      }
    }
  }

  // Observe DOM for new message content
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      // Check added nodes
      mutation.addedNodes.forEach(function(node) {
        if (node.nodeType === 1) {
          checkForDashboardMarker(node);
          // Also check child elements
          if (node.querySelectorAll) {
            node.querySelectorAll('*').forEach(checkForDashboardMarker);
          }
        } else if (node.nodeType === 3) {
          // Text node
          checkForDashboardMarker(node.parentElement);
        }
      });

      // Check if text content changed
      if (mutation.type === 'characterData') {
        checkForDashboardMarker(mutation.target.parentElement);
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
    document.querySelectorAll('*').forEach(checkForDashboardMarker);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startObserving);
  } else {
    startObserving();
  }
})();
