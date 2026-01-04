"use client";

import { useState, useEffect } from "react";

interface DashboardInfo {
  host: string;
  port: number;
}

export function useDashboardPort(): DashboardInfo | null {
  const [dashboard, setDashboard] = useState<DashboardInfo | null>(null);

  useEffect(() => {
    const handler = (event: MessageEvent) => {
      if (event.data?.type === "DASHBOARD_PORT" && event.data.host && event.data.port) {
        setDashboard({ host: event.data.host, port: event.data.port });
      }
    };
    window.addEventListener("message", handler);
    return () => window.removeEventListener("message", handler);
  }, []);

  return dashboard;
}
