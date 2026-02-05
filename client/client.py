from mcp.client import Client
from openai import OpenAI

# Connect to MCP server
client = Client()
client.connect("log-file-analyzer")

# Initialize LLM
llm = OpenAI()

# Ask a question
question = "Explain the errors in the log file app.log"

# Run MCP + LLM
response = client.run(
    llm=llm,
    prompt=question,
    tools=["read_log_file"]
)

print("\n--- AI RESPONSE ---\n")
print(response)
