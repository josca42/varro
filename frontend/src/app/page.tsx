import { Header } from "@/components/layout/header";
import { SplitView } from "@/components/layout/split-view";

export default function Home() {
  return (
    <div className="flex flex-col h-screen">
      <Header />
      <SplitView />
    </div>
  );
}
