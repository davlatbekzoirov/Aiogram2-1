from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Запустить бота",
            "/help - Команды бота",
            "/auto_comment - Сгенерировать текст",
            "/chat_gpt - Чат с GPT-3",
            "/generate_image - Сгенерировать изображение")
    
    await message.answer("\n".join(text))