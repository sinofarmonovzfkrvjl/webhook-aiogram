# app.py
from flask import Flask, request, jsonify
from main import dp, bot
from aiogram.types import Update
import asyncio

app = Flask(__name__)

WEBHOOK_PATH = "/webhook/bot"
WEBHOOK_URL = f"https://webhook-aiogram.onrender.com{WEBHOOK_PATH}"

@app.route(WEBHOOK_PATH, methods=['POST'])
def telegram_webhook():
    update = Update(**request.json)
    asyncio.run(dp.feed_update(bot, update))
    return jsonify({"status": "ok"})

@app.before_first_request
def setup_webhook():
    asyncio.run(bot.set_webhook(WEBHOOK_URL))

@app.teardown_appcontext
def shutdown_webhook(exception=None):
    asyncio.run(bot.delete_webhook())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
