from fastmcp import FastMCP
import random

mcp: FastMCP = FastMCP("add-some-numbers")

SILLY_GREETINGS = [
    "Howdy-doody",
    "Well butter my biscuit",
    "Holy guacamole",
    "Great galloping galoshes",
    "Sweet sassy molassy",
    "Well slap me with a wet noodle",
    "Jumpin' Jehosaphat",
    "Great Caesar's ghost",
    "Cheese and crackers",
    "Well I'll be a monkey's uncle"
]

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    greeting = random.choice(SILLY_GREETINGS)
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8001,
    )
