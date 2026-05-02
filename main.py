# ====== ИМПОРТЫ ======
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
import requests  # нужен чтобы отправлять запрос в бота

app = FastAPI()

# 🔐 Секрет (должен совпадать с ботом)
SECRET_KEY = "123456"

# 🤖 Ссылка на бота (ВАЖНО: вставь свой домен бота)
BOT_API_URL = "https://ТВОЙ-БОТ.up.railway.app/reward"

# ====== ПРОВЕРКА (чтобы не было 502) ======
@app.get("/")
async def home():
    return {"status": "ok"}

# ====== СТРАНИЦА ЗАДАНИЯ ======
@app.get("/task")
async def task(click_id: str):
    return HTMLResponse(f"""
    <html>
    <body style="text-align:center;font-family:sans-serif;">
        <h2>📋 Выполни задание</h2>
        <p>Нажми кнопку и выполни действие</p>

        <!-- КНОПКА -->
        <button id="btn" disabled style="padding:15px 25px;font-size:18px;">
            Перейти к заданию
        </button>

        <script>
            // ⏳ Задержка 3 секунды (анти-бот)
            setTimeout(() => {{
                document.getElementById("btn").disabled = false;
            }}, 3000);

            // 🔗 Переход на /go
            document.getElementById("btn").onclick = () => {{
                window.location.href = "/go?click_id={click_id}";
            }};
        </script>
    </body>
    </html>
    """)

# ====== РЕДИРЕКТ НА ОФФЕР ======
@app.get("/go")
async def go(click_id: str):
    # 👉 пока тест (потом заменишь на реальный оффер)
    offer_link = f"https://google.com/?subid={click_id}"

    return RedirectResponse(offer_link)

# ====== POSTBACK (ИМИТАЦИЯ) ======
@app.get("/postback")
async def postback(click_id: str, key: str):
    # 🔐 проверка ключа
    if key != SECRET_KEY:
        return JSONResponse({"status": "error"})

    # 📩 отправляем запрос в бота (начисление баллов)
    try:
        requests.get(f"{BOT_API_URL}?click_id={click_id}&key={SECRET_KEY}")
    except:
        return JSONResponse({"status": "bot_error"})

    return JSONResponse({"status": "ok"})