from fastmcp import FastMCP

# Create a proxy to the remote FastMCP Cloud server
# FastMCP Cloud uses Streamable HTTP (default) - use the /mcp URL
mcp = FastMCP.as_proxy(
    "https://splendid-gold-dingo.fastmcp.app/mcp",  # Standard FastMCP Cloud URL
    name="Nitish Server Proxy"
)

if __name__ == "__main__":
    # Runs via stdio - local server
    mcp.run()