import os
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("example-mcp")


@mcp.tool(description="A simple tool that returns a greeting message.")
async def hello() -> str:
    return f"Hello, I am {os.environ.get('MCP_NAME')}!"

def main():
    mcp.run()


if __name__ == '__main__':
    main()
