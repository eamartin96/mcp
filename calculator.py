from fastmcp import FastMCP
mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def sub(a: int, b: int) -> float:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    mcp.run()
