export function Header() {
  return (
    <header className="flex items-center justify-between h-14 px-4 border-b bg-background">
      <div className="flex items-center gap-2">
        <span className="text-lg font-semibold">Varro</span>
        <span className="text-sm text-muted-foreground">Data Analysis</span>
      </div>
    </header>
  );
}
