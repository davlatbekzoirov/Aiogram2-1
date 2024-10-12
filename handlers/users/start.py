from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"<b>Your full name,</b> {message.from_user.full_name}!",
        f"<b>Your chat ID:</b> {message.from_user.chat.id}",
        f"<b>Your user ID:</b> {message.from_user.id}",
        f"<b>Your username:</b> {message.from_user.username}")