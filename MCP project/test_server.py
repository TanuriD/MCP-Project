#!/usr/bin/env python3
"""
Test client for MCP File Server

This script demonstrates how to test the MCP server functionality
by simulating file operations.
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path to import file_server
sys.path.insert(0, str(Path(__file__).parent))

from file_server import upload_file, read_file, list_files, analyze_file


async def test_upload():
    """Test file upload functionality."""
    print("\n📤 Testing file upload...")
    
    # Test valid upload
    result = await upload_file({
        "filename": "test.txt",
        "content": "Hello, MCP! This is a test file.\nIt has multiple lines.\nAnd some content to analyze."
    })
    print(f"  {result[0].text}")
    
    # Test another file
    result = await upload_file({
        "filename": "example.txt",
        "content": "This is an example file with some sample content."
    })
    print(f"  {result[0].text}")


async def test_list():
    """Test file listing functionality."""
    print("\n📋 Testing file listing...")
    
    result = await list_files({})
    print(f"  {result[0].text}")


async def test_read():
    """Test file reading functionality."""
    print("\n📖 Testing file reading...")
    
    # Test reading existing file
    result = await read_file({"filename": "test.txt"})
    print(f"  {result[0].text}")
    
    # Test reading non-existent file
    print("\n  Testing error handling (non-existent file):")
    result = await read_file({"filename": "nonexistent.txt"})
    print(f"  {result[0].text}")


async def test_analyze():
    """Test file analysis functionality."""
    print("\n📊 Testing file analysis...")
    
    result = await analyze_file({"filename": "test.txt"})
    print(f"  {result[0].text}")


async def test_security():
    """Test security validation."""
    print("\n🔒 Testing security (path traversal prevention)...")
    
    # Test path traversal attempt
    result = await upload_file({
        "filename": "../malicious.txt",
        "content": "This should be blocked"
    })
    print(f"  {result[0].text}")
    
    # Test another path traversal attempt
    result = await read_file({"filename": "../../etc/passwd"})
    print(f"  {result[0].text}")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("🧪 MCP File Server - Test Suite")
    print("=" * 60)
    
    await test_upload()
    await test_list()
    await test_read()
    await test_analyze()
    await test_security()
    
    print("\n" + "=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
