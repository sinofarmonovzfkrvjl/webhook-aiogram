# bot.py
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

API_TOKEN = '7596605488:AAHImzVpR__WfikvzT-gFRgZL0vfTd5T1cs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello! I am a webhook-based bot.")
