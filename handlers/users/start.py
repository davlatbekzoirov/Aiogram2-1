from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests, sqlite3, datetime
from data.config import API_KEY
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    try:
        user_get = await bot.get_chat(message.from_user.id)
        user_bio = user_get.bio    
        db.add_user(id=message.from_user.id,fullname=message.from_user.full_name,username=message.from_user.username)
        count = db.count_users()[0]
        await bot.send_message(chat_id='-1002077533723',text=f"""
🆕 Yangi foydalanuvchi!
🆔 Foydalanuvchi identifikatori: {message.from_user.id}
📛 Foydalanuvchi: {message.from_user.get_mention()}
🌐 Foydalanuvchi nomi: {message.from_user.username}
📍 Foydalanuvchining tarjimai holi: {user_bio}
➖➖➖➖➖➖➖➖➖➖➖
🖐Jami: {count}""")
    except sqlite3.IntegrityError as err:pass

    await message.answer(f"Salom {message.from_user.full_name}!") 
