from fastmcp import FastMCP

mcp: FastMCP = FastMCP("add-some-numbers")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        port=8001,
    )
