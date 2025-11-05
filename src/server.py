#!/usr/bin/env python3
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MailDriveCopilot")

@mcp.tool()
def ping() -> str:
    """Health check."""
    return "ok"

@mcp.tool()
def draft_reply(thread_subject: str, key_points: list[str]) -> str:
    """Return a suggested reply from a subject + bullet points (demo only)."""
    bullets = "\n".join(f"- {p}" for p in key_points)
    return (
        f"Subject: Re: {thread_subject}\n\n"
        f"Hi,\n\nThanks for the update. Here are the points I'm addressing:\n{bullets}\n\n"
        "Best regards,\nAli"
    )

if __name__ == "__main__":
    print("MCP server stub is alive.")
    print("Configured users:", os.getenv("GMAIL_USER", "n/a"), os.getenv("MS_USER", "n/a"))