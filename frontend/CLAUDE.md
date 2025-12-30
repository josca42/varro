## Frontend

Next.js app with split-pane layout embedding two iframes.

## Commands

```bash
npm run dev      # Start dev server (port 3000)
npm run build    # Production build
```

## Structure

```
src/
  app/
    page.tsx           # Main page (Header + SplitView)
    layout.tsx         # Root layout
    globals.css        # Tailwind styles

  components/
    layout/
      header.tsx       # App header
      split-view.tsx   # ResizablePanelGroup with chat + dashboard

    chat/
      chat-iframe.tsx  # Embeds Chainlit (localhost:8026)

    dashboard/
      dashboard-iframe.tsx      # Embeds Evidence dashboard
      dashboard-placeholder.tsx # Shown when no dashboard

    ui/                # Shadcn components

  hooks/
    use-dashboard-port.ts  # Listens for postMessage with dashboard port
```

## Communication

1. Backend sends `<!--DASHBOARD_PORT:xxx-->` in chat message
2. Custom JS in Chainlit (`dashboard.js`) detects marker
3. Posts `{ type: 'DASHBOARD_PORT', port }` to parent window
4. `useDashboardPort` hook receives message, updates iframe src

## Environment

```
NEXT_PUBLIC_CHAINLIT_URL=http://localhost:8026
```
