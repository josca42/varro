"use client";

import { useDashboardPort } from "@/hooks/use-dashboard-port";
import { DashboardPlaceholder } from "./dashboard-placeholder";

export function DashboardIframe() {
  const dashboard = useDashboardPort();

  if (!dashboard) {
    return <DashboardPlaceholder />;
  }

  return (
    <iframe
      src={`http://${dashboard.host}:${dashboard.port}`}
      className="w-full h-full border-0"
      title="Evidence Dashboard"
      key={`${dashboard.host}:${dashboard.port}`}
    />
  );
}
