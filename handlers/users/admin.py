import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
import logging
from keyboards.inline.menu_keyboards import buy_item

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        await bot.send_message(
            chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!"
        )
        await asyncio.sleep(0.05)

@dp.callback_query_handler(lambda query: query.data == 'buy')
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != ADMINS:
        try:
            await bot.send_message(ADMINS, f"Сообщение от пользователя {callback_query.from_user.id}: {callback_query.data}")
            await bot.answer_callback_query(callback_query.id, "Сообщение отправлено администратору", show_alert=True)
        except Exception as e:
            logging.exception(e)

@dp.message_handler()
async def forward_to_admin(message: types.Message):
    if message.from_user.id != ADMINS[0]:
        try:
            await bot.send_message(ADMINS[0], f"Foydalanuvchidan habar \nID = {message.from_user.id}:\nIsm = {message.from_user.username}:\n\n {message.text}")
        except Exception as e:
            logging.exception(e)
