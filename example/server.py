from fastmcp import FastMCP
mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    """Returns a greeting message for the givem name."""
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
