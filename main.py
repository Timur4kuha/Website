from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# ====== ГЛАВНАЯ СТРАНИЦА ======
@app.get("/")
async def home():
    return {"status": "ok"}

# ====== СТРАНИЦА САЙТА ======
@app.get("/task")
async def task():
    return HTMLResponse("""
    <html>
    <body style="text-align:center;font-family:sans-serif;">
        <h1>Сайт работает ✅</h1>
        <p>Если ты это видишь — всё настроено правильно</p>

        <button onclick="alert('Кнопка работает!')" 
        style="padding:15px 25px;font-size:18px;">
            Нажми меня
        </button>
    </body>
    </html>
    """)

# ====== ЗАПУСК (ВАЖНО ДЛЯ RAILWAY) ======
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)