# MCP File Upload & Reader Application

This project demonstrates how to build a simple application using
**Model Context Protocol (MCP)** that allows an AI client to:

-   Upload text files to a server
-   Read uploaded files
-   Process file content using MCP tools

It is designed as a reference implementation for tool-based AI systems
and agent architectures.

------------------------------------------------------------------------

## Features

-   MCP server with file handling tools
-   Upload files using AI tool calls
-   Read stored files
-   Optional file analysis (word count, characters, etc.)
-   Uses STDIO transport (local, fast, simple)

------------------------------------------------------------------------

## Architecture

    AI Client (Claude / Agent / App)
            |
            v
         MCP Client
            |
            v
         MCP Server
        ├── upload_file()
        └── read_file()

------------------------------------------------------------------------

## Tech Stack

-   Python 3.9+
-   MCP Python SDK
-   Local file system storage

------------------------------------------------------------------------

## Project Structure

    .
    ├── file_server.py
    ├── uploads/
    └── README.md

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

``` bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

``` bash
pip install mcp
```

------------------------------------------------------------------------

## Running the MCP Server

Start the server using:

``` bash
python file_server.py
```

The server will start using STDIO transport and wait for MCP client
connections.

------------------------------------------------------------------------

## Connecting Using Claude Desktop (Optional)

1.  Open Claude Desktop configuration file.

2.  Add:

``` json
{
  "mcpServers": {
    "fileServer": {
      "command": "python",
      "args": ["file_server.py"]
    }
  }
}
```

3.  Restart Claude Desktop.

------------------------------------------------------------------------

## Available Tools

### upload_file

Uploads a text file to the server.

**Parameters:** - `filename` (string) - `content` (string)

------------------------------------------------------------------------

### read_file

Reads an uploaded file.

**Parameters:** - `filename` (string)

------------------------------------------------------------------------

## Example Usage (via AI Client)

Upload a file:

    Upload a file named example.txt with content "Hello MCP"

Read the file:

    Read the file example.txt

------------------------------------------------------------------------

## Optional: File Analysis Tool

You can extend the server with additional tools such as:

-   Word count
-   Character count
-   Summarization
-   Embedding generation

------------------------------------------------------------------------

## Security Notes

For production usage:

-   Validate filenames
-   Restrict file extensions
-   Limit file size
-   Use sandbox directories
-   Add authentication for HTTP-based MCP servers

------------------------------------------------------------------------

## Future Improvements

-   HTTP transport support
-   Web frontend for file uploads
-   Support for PDF/DOCX files
-   Vector database integration
-   Multi-user authentication
-   Docker deployment

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

## Author

`<Your Name>`{=html}

------------------------------------------------------------------------

## References

-   MCP Specification
-   Anthropic MCP SDK Documentation
