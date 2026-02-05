from mcp.server import Server
import os

#create mcp server
server = Server("log-file-analyzer")

#only allow reading from logs folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

@server.tool()
def read_log_file(file_name: str) -> str:
    """
    Read a log file and return its contents.
    """
    file_path = os.path.join(LOG_DIR, file_name)

    if not os.path.exists(file_path):
        return "log file not found."
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    server.run()
  