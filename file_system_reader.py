import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(os.getenv("FILE_READER_DIRECTORY", "./documents"))

mpc = FastMCP("file-system-reader")

@mpc.tool()
def read_file(filename: str) -> str:
    "Read a file from the document or any given directory."

    try:    
       file_path = BASE_DIR / filename
       if not str(file_path.resolve()).startswith(str(BASE_DIR.resolve())) :
           return "Access denied - invalid path"
       content = file_path.read_text(encoding="utf-8")
       return f"File :{filename}\n\n{content}"

    except Exception as exception:
        return f"Error reading the given file: {exception}"
    
@mpc.tool()
def list_files() -> str:
    "List files in directory"
    try: 
        files = [f.name for f in BASE_DIR.iterdir() if f.is_file()]
        files_text = "\n".join(sorted(files)) if files else "No files found"
        return f"Files:\n\n{files_text}"
    
    except Exception as exception:
        return f"Error listing file: {exception}"

