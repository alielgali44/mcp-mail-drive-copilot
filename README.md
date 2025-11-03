# mcp-mail-drive-copilot

**What it is:** A tiny MCP server that lets an AI assistant (Claude/ChatGPT with MCP) read a mail thread, find referenced files (Drive/OneDrive), summarize, and draft a reply.

**Why MCP:** MCP is the open standard (“USB-C for AI”) to connect models to real tools. https://modelcontextprotocol.io

## Quick start
1) Create `.env` (scopes are least-privilege/read-only first):
   - Gmail/Drive: GOOGLE_CREDENTIALS_JSON, GMAIL_USER
   - Microsoft Graph (Mail/Files): MSGRAPH_TENANT_ID, MSGRAPH_CLIENT_ID, MSGRAPH_CLIENT_SECRET, MS_USER
2) Run the server (Python/Node stub; code coming soon).
3) Add this MCP server in your MCP client (Claude Desktop / ChatGPT Apps).

## Example prompts
- “Summarize the latest thread with {{Name}}, find the referenced contract in Drive, and draft a polite follow-up.”
- “Search OneDrive for ‘Q3 report’, include link in the reply, propose 3 subject lines.”

## Security
- Least-privilege scopes; confirm-before-send; tokens in Keychain/.env (never in prompts).
