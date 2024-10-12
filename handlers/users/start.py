from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, ContentType
from keyboards.inline.zabrat_skidku import zabrat_skidku
# import asyncpg
# from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # try:
    #     user = await db.add_user(telegram_id=message.from_user.id,
    #                              full_name=message.from_user.full_name,
    #                              username=message.from_user.username)
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id=message.from_user.id)
    album = types.MediaGroup()
    photo_id_1 = "AgACAgIAAxkBAAIBdWV3RUgVhRq4c6kzvlZmlF5KoiWJAAIF2jEborTAS4YPQw0_b1QnAQADAgADeQADMwQ"
    photo_id_2 = "AgACAgIAAxkBAAIBd2V3RXaaEZm7Q_EzmXrzVJflWOYAAwfaMRuitMBLjmxwltQ6zwsBAAMCAAN5AAMzBA"
    photo_id_3 = "AgACAgIAAxkBAAIBeWV3RYckmazB3jcyy4p_4gl_C8sCAAIJ2jEborTAS5JCvrYb6HAxAQADAgADeQADMwQ"
    photo_id_4 = "AgACAgIAAxkBAAIBe2V3RcN0j-7gSY9rz2Da6yUYw1B3AAIK2jEborTAS5J8ah-sypgQAQADAgADeQADMwQ"
    photo_id_5 = "AgACAgIAAxkBAAIBfWV3RdYwWbsdNds-tZbZuBfo-xC6AAIL2jEborTAS08W_GPLQva-AQADAgADeQADMwQ"
    photo_id_6 = "AgACAgIAAxkBAAIBf2V3ReoY3RUf7iBt6Ze39Neeyh6QAAIO2jEborTASy9UBje8vUxiAQADAgADeQADMwQ"
    await message.answer("Привет! 😇 Смотри, какую классную фотокнигу можем напечатать и отправить прямо сейчас. Тебе или твоим близким! 👇")
    album.attach_photo(photo=photo_id_1)
    album.attach_photo(photo=photo_id_2)
    album.attach_photo(photo=photo_id_3)
    album.attach_photo(photo=photo_id_4)
    album.attach_photo(photo=photo_id_5)
    album.attach_photo(photo=photo_id_6)
    await message.reply_media_group(media=album)
    msg = "Фотокнига будет большая - 20*20 см.\n"
    msg += "Дарю тебе скидку 10% на первый заказ. С ней фотокнигу можно заказать от 2880 руб 3200 руб!\n"
    msg += "❣️ Cкидка будет активна только 3 дня после запуска бота.\n"
    msg += "Так что скорее жми на кнопку ниже, чтобы забрать скидку! 👇"
    await bot.send_message(chat_id=message.from_user.id, text=msg, reply_markup=zabrat_skidku)

    # count = await db.count_users()
    # msg = f"{user[1]} добавлен в базу. Текущее количество пользователей в базе {count}"
    # await bot.send_message(chat_id=ADMINS[0], text=msg)