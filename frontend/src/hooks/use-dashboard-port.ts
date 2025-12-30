"use client";

import { useState, useEffect } from "react";

export function useDashboardPort() {
  const [port, setPort] = useState<number | null>(null);

  useEffect(() => {
    const handler = (event: MessageEvent) => {
      if (event.data?.type === "DASHBOARD_PORT") {
        setPort(event.data.port);
      }
    };
    window.addEventListener("message", handler);
    return () => window.removeEventListener("message", handler);
  }, []);

  return port;
}
