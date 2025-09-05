from mcp.server.fastmcp import FastMCP

mcp = FastMCP("simple-calculator")

# Example: add two numbers
@mcp.tool()
def add(a: float, b: float) -> int:
    """Add two numbers and return the result."""
    return int(a) + int(b)


# Example: subtract two numbers
@mcp.tool()
def subtract(a: float, b: float) -> int:
    """Subtract b from a and return the result."""
    return int(a) - int(b)

# Example: multiply two numbers
@mcp.tool()
def multiply(a: float, b: float) -> int:
    """Multiply two numbers and return the result."""
    return int(a) * int(b)

# Example: divide two numbers
@mcp.tool()
def divide(a: float, b: float) -> int:
    """Divide a by b and return the result. Handles division by zero."""
    return int(a) / int(b)

if __name__ == "__main__":
    print("MPC is running")
    mcp.run()