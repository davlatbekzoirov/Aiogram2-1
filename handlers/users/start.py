from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет! Я бот, который использует GPT-3 для комментирования в каналах Telegram. Отправьте мне текст, и я сгенерирую комментарий на основе вашего сообщения.")
