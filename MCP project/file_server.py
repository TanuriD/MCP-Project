#!/usr/bin/env python3
"""
MCP File Upload & Reader Server

This server provides tools for uploading and reading text files
using the Model Context Protocol (MCP).
"""

import os
import asyncio
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


# Initialize MCP server
app = Server("file-server")

# Define upload directory
UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


def validate_filename(filename: str) -> bool:
    """
    Validate filename to prevent directory traversal attacks.
    
    Args:
        filename: The filename to validate
        
    Returns:
        True if filename is valid, False otherwise
    """
    # Check for directory traversal attempts
    if ".." in filename or "/" in filename or "\\" in filename:
        return False
    
    # Check for empty filename
    if not filename or filename.strip() == "":
        return False
    
    return True


@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    List available MCP tools.
    
    Returns:
        List of available tools
    """
    return [
        Tool(
            name="upload_file",
            description="Upload a text file to the server. The file will be stored in the uploads directory.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Name of the file to upload (e.g., 'example.txt')"
                    },
                    "content": {
                        "type": "string",
                        "description": "Text content to write to the file"
                    }
                },
                "required": ["filename", "content"]
            }
        ),
        Tool(
            name="read_file",
            description="Read the contents of an uploaded file from the server.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Name of the file to read (e.g., 'example.txt')"
                    }
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="list_files",
            description="List all uploaded files in the uploads directory.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="analyze_file",
            description="Analyze an uploaded file and return statistics (word count, character count, line count).",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Name of the file to analyze (e.g., 'example.txt')"
                    }
                },
                "required": ["filename"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """
    Handle tool calls from MCP client.
    
    Args:
        name: Name of the tool to call
        arguments: Arguments passed to the tool
        
    Returns:
        List of text content responses
    """
    if name == "upload_file":
        return await upload_file(arguments)
    elif name == "read_file":
        return await read_file(arguments)
    elif name == "list_files":
        return await list_files(arguments)
    elif name == "analyze_file":
        return await analyze_file(arguments)
    else:
        return [TextContent(
            type="text",
            text=f"Error: Unknown tool '{name}'"
        )]


async def upload_file(arguments: dict) -> list[TextContent]:
    """
    Upload a file to the server.
    
    Args:
        arguments: Dictionary containing 'filename' and 'content'
        
    Returns:
        Success or error message
    """
    try:
        filename = arguments.get("filename", "")
        content = arguments.get("content", "")
        
        # Validate filename
        if not validate_filename(filename):
            return [TextContent(
                type="text",
                text=f"Error: Invalid filename '{filename}'. Filename must not contain path separators or '..'."
            )]
        
        # Create file path
        file_path = UPLOAD_DIR / filename
        
        # Write content to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return [TextContent(
            type="text",
            text=f"✓ Successfully uploaded '{filename}' ({len(content)} characters)"
        )]
        
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error uploading file: {str(e)}"
        )]


async def read_file(arguments: dict) -> list[TextContent]:
    """
    Read a file from the server.
    
    Args:
        arguments: Dictionary containing 'filename'
        
    Returns:
        File content or error message
    """
    try:
        filename = arguments.get("filename", "")
        
        # Validate filename
        if not validate_filename(filename):
            return [TextContent(
                type="text",
                text=f"Error: Invalid filename '{filename}'. Filename must not contain path separators or '..'."
            )]
        
        # Create file path
        file_path = UPLOAD_DIR / filename
        
        # Check if file exists
        if not file_path.exists():
            return [TextContent(
                type="text",
                text=f"Error: File '{filename}' not found in uploads directory."
            )]
        
        # Read file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        return [TextContent(
            type="text",
            text=f"Content of '{filename}':\n\n{content}"
        )]
        
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error reading file: {str(e)}"
        )]


async def list_files(arguments: dict) -> list[TextContent]:
    """
    List all files in the uploads directory.
    
    Args:
        arguments: Empty dictionary
        
    Returns:
        List of files or error message
    """
    try:
        files = [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]
        
        if not files:
            return [TextContent(
                type="text",
                text="No files found in uploads directory."
            )]
        
        files_list = "\n".join([f"  • {f}" for f in sorted(files)])
        return [TextContent(
            type="text",
            text=f"Uploaded files ({len(files)}):\n{files_list}"
        )]
        
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error listing files: {str(e)}"
        )]


async def analyze_file(arguments: dict) -> list[TextContent]:
    """
    Analyze a file and return statistics.
    
    Args:
        arguments: Dictionary containing 'filename'
        
    Returns:
        File statistics or error message
    """
    try:
        filename = arguments.get("filename", "")
        
        # Validate filename
        if not validate_filename(filename):
            return [TextContent(
                type="text",
                text=f"Error: Invalid filename '{filename}'. Filename must not contain path separators or '..'."
            )]
        
        # Create file path
        file_path = UPLOAD_DIR / filename
        
        # Check if file exists
        if not file_path.exists():
            return [TextContent(
                type="text",
                text=f"Error: File '{filename}' not found in uploads directory."
            )]
        
        # Read and analyze file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Calculate statistics
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(content.splitlines())
        
        stats = f"""File Analysis: '{filename}'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Characters: {char_count:,}
Words:      {word_count:,}
Lines:      {line_count:,}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
        
        return [TextContent(
            type="text",
            text=stats
        )]
        
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error analyzing file: {str(e)}"
        )]


async def main():
    """
    Main entry point for the MCP server.
    """
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    # Note: When using STDIO transport, do not print to stdout
    # as it interferes with JSON-RPC communication
    asyncio.run(main())

