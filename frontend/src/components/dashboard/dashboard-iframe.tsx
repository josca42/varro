"use client";

import { useDashboardPort } from "@/hooks/use-dashboard-port";
import { DashboardPlaceholder } from "./dashboard-placeholder";

export function DashboardIframe() {
  const port = useDashboardPort();

  if (!port) {
    return <DashboardPlaceholder />;
  }

  return (
    <iframe
      src={`http://localhost:${port}`}
      className="w-full h-full border-0"
      title="Evidence Dashboard"
      key={port}
    />
  );
}
