# MCP File Upload & Reader - Quick Start Guide

## 🚀 Quick Start

### 1. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Run the Server

```bash
python file_server.py
```

You should see:
```
🚀 Starting MCP File Server...
📁 Upload directory: C:\Users\Admin\Desktop\MCP project\uploads
⏳ Waiting for MCP client connection...
```

### 3. Test the Server

In a new terminal (with venv activated):
```bash
python test_server.py
```

---

## 🔧 Available Tools

### 1. upload_file
Upload a text file to the server.

**Parameters:**
- `filename` (string) - Name of the file
- `content` (string) - File content

**Example:**
```
Upload a file named "notes.txt" with content "My important notes"
```

### 2. read_file
Read an uploaded file.

**Parameters:**
- `filename` (string) - Name of the file to read

**Example:**
```
Read the file "notes.txt"
```

### 3. list_files
List all uploaded files.

**Example:**
```
List all uploaded files
```

### 4. analyze_file
Get statistics about a file.

**Parameters:**
- `filename` (string) - Name of the file to analyze

**Example:**
```
Analyze the file "notes.txt"
```

---

## 🔗 Claude Desktop Integration

### Step 1: Locate Claude Desktop Config

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Mac:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Step 2: Add Server Configuration

Add this to your config file:

```json
{
  "mcpServers": {
    "fileServer": {
      "command": "python",
      "args": ["file_server.py"],
      "cwd": "c:\\Users\\Admin\\Desktop\\MCP project",
      "env": {}
    }
  }
}
```

**Note:** Update the `cwd` path to match your project location.

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop to load the new configuration.

### Step 4: Use with Natural Language

You can now use commands like:
- "Upload a file called todo.txt with my tasks"
- "Show me the content of todo.txt"
- "List all my files"
- "Analyze the file todo.txt"

---

## 🛡️ Security Features

- ✅ Filename validation (no path traversal)
- ✅ Sandboxed uploads directory
- ✅ Input sanitization
- ✅ Error handling

---

## 📁 File Storage

All uploaded files are stored in:
```
./uploads/
```

---

## 🐛 Troubleshooting

### Server won't start
- Check if virtual environment is activated
- Verify MCP package is installed: `pip list | grep mcp`

### Can't upload files
- Ensure uploads directory exists
- Check filename doesn't contain `/`, `\`, or `..`

### Claude Desktop not connecting
- Verify config file path is correct
- Check server is running
- Restart Claude Desktop

---

## 💡 Tips

1. **Keep the server running** while using with Claude Desktop
2. **Check uploads folder** to see stored files
3. **Use test_server.py** to verify functionality
4. **Read error messages** - they provide helpful feedback

---

## 📚 Additional Resources

- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- Project README: [README.md](README.md)
