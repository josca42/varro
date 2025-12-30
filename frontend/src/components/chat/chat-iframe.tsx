"use client";

const CHAINLIT_URL = process.env.NEXT_PUBLIC_CHAINLIT_URL || "http://localhost:8026";

export function ChatIframe() {
  return (
    <iframe
      src={CHAINLIT_URL}
      className="w-full h-full border-0"
      title="Chat"
      allow="clipboard-read; clipboard-write"
    />
  );
}
