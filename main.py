import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Главная страница (проверка что сайт работает)
@app.get("/")
def home():
    return {"status": "ok"}

# Railway порт (ВАЖНО!)
port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)