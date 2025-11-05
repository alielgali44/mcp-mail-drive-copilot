# MCP Mail & Drive Copilot

A tiny **MCP** server that lets an AI assistant (Claude/ChatGPT with MCP) work with mail threads and files:
- Read a thread subject you provide
- (Later) look up referenced files (Drive/OneDrive)
- Summarize & draft a reply (demo tool included)

**What is MCP?** The Model Context Protocol is the open standard (“USB-C for AI”) for connecting models to tools & data. Learn more: modelcontextprotocol.io and Claude’s MCP guide.  
- MCP site: https://modelcontextprotocol.io  
- Claude MCP docs: https://docs.claude.com/en/docs/mcp  
- OpenAI Apps SDK + MCP servers: https://developers.openai.com/apps-sdk/concepts/mcp-server

## Quick start
**Prereqs**: Python 3.10+, `pip`  
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # add your values later
python src/server.py   # dev: prints server is alive