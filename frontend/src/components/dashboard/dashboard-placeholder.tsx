import { Card, CardContent } from "@/components/ui/card";

export function DashboardPlaceholder() {
  return (
    <div className="flex items-center justify-center h-full bg-muted/30">
      <Card className="w-96">
        <CardContent className="pt-6">
          <div className="text-center space-y-2">
            <div className="text-4xl mb-4">📊</div>
            <h3 className="text-lg font-medium">No Dashboard Yet</h3>
            <p className="text-sm text-muted-foreground">
              Start a conversation in the chat to create a dashboard. Ask the AI
              to analyze data and generate visualizations.
            </p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
