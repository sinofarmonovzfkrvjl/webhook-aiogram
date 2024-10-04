# app.py
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from main import bot, dp

WEBHOOK_URL = 'https://webhook-aiogram.onrender.com/webhook/bot'

async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()

def main():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook/bot")
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host="0.0.0.0", port=8080)

if __name__ == '__main__':
    main()
