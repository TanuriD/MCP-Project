import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["../server/mcp_server.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call the read_log_file tool with correct filename
            result = await session.call_tool(
                "read_log_file",
                {"filename": "app.log"}  # Changed from "sample.log" to "app.log"
            )

            print("Tool response:")
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())