"use client";

import {
  ResizablePanelGroup,
  ResizablePanel,
  ResizableHandle,
} from "@/components/ui/resizable";
import { ChatIframe } from "@/components/chat/chat-iframe";
import { DashboardIframe } from "@/components/dashboard/dashboard-iframe";

export function SplitView() {
  return (
    <ResizablePanelGroup direction="horizontal" className="flex-1">
      <ResizablePanel defaultSize={50} minSize={25}>
        <ChatIframe />
      </ResizablePanel>
      <ResizableHandle withHandle />
      <ResizablePanel defaultSize={50} minSize={25}>
        <DashboardIframe />
      </ResizablePanel>
    </ResizablePanelGroup>
  );
}
