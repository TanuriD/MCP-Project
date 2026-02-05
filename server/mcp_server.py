from mcp.server.fastmcp import FastMCP
import os

# Create MCP app
mcp = FastMCP("log-file-analyzer")

# Path to logs directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")


@mcp.tool()
def read_log_file(filename: str) -> str:
    """
    Read a log file and return its contents.
    """
    file_path = os.path.join(LOG_DIR, filename)

    if not os.path.exists(file_path):
        return "Log file not found."

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    mcp.run()
