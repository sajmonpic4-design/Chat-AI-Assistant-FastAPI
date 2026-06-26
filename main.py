import re
import subprocess
from fastapi import FastAPI
from pydantic import BaseModel

from pathlib import Path
from fastapi.responses import FileResponse, JSONResponse

ANSI_ESCAPE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()

class Msg(BaseModel):
    content: str

@app.get("/", response_class=FileResponse)
def read_root():
    return BASE_DIR / "index.html"

def strip_ansi(text: str) -> str:
    return ANSI_ESCAPE.sub("", text).replace("\r", "")

def remove_consecutive_duplicate_words(text: str) -> str:
    words = text.split()
    filtered = []
    prev = None
    for word in words:
        normalized = re.sub(r'^[^\w]+|[^\w]+$', '', word, flags=re.UNICODE).casefold()
        if normalized != prev:
            filtered.append(word)
            prev = normalized
    return " ".join(filtered)

@app.post("/chat")
def chat(msg: Msg):
    result = subprocess.run(
        ["ollama", "run", "llama3.1:8b", msg.content],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    stdout = remove_consecutive_duplicate_words(strip_ansi(result.stdout)).strip()
    stderr = strip_ansi(result.stderr).strip()
    if result.returncode != 0:
        return JSONResponse(
            status_code=500,
            content={"error": "Ollama failed", "detail": stderr},
        )
    return {"reply": stdout}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)