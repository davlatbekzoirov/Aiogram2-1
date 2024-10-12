from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, ContentType
from keyboards.inline.zabrat_skidku import refresh_bot, upload_media
from .zabrat_skidku import photo_count

user_orders = {}

@dp.message_handler(commands="orders")
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    orders = user_orders.get(user_id, [])

    if not orders:
        msg = "У вас пока нет заказов."
    else:
        msg = "Ваши последние заказы:\n"
        for order_number, photo_count in enumerate(orders, start=1):
            msg += f"Заказ #{order_number}: {photo_count} фото\n"

    msg += "\nЕсли у вас есть вопросы, обращайтесь в поддержку!"
    await message.reply(msg, reply_markup=refresh_bot)
 

@dp.callback_query_handler(text = "refresh_bo1")
async def adgj(call: CallbackQuery):
    user_id = call.from_user.id
    orders = user_orders.get(user_id, [])
    msg = "Ваши последние заказы:\n"
    for order_number, photo_count in enumerate(orders, start=1):
        msg += f"Заказ #{order_number}: {photo_count} фото\n"

    msg += "\nЕсли у вас есть вопросы, обращайтесь в поддержку!"
    await call.message.answer(msg, reply_markup=refresh_bot)
    
@dp.callback_query_handler(text = "refresh_bot2")
async def adgj(call: CallbackQuery):
    video = "BAACAgIAAxkBAAICNWV3WRytoy3qE1jJU0S3DsWQz0Q6AAIrMQACre7ASYApVbKl1FS7MwQ"
    await bot.send_video(chat_id=call.message.chat.id, video=video)
    msg = "Сначала давай сделаем самое важное - загрузим фотки для фотокниги!\n"
    msg += "Размер альбома - 20*20 см. На каждом развороте - по 2 фотки. C твоей скидкой такой разворот будет стоить 288 руб  320 руб! \n"
    msg += "Необходимо загрузить от 20 до 60 фото.\n"
    msg += "Я сам создам фотокнигу, тебе надо просто скинуть фотки в пару кликов!\n"
    msg += "Если будут любые вопросы, можешь написать нам в <a href='https://t.me/your_kind_support'>личку</a>. Мы на связи и сразу поможем!\n"
    msg += "👇 Жми на кнопку ниже, чтобы загрузить фотки:\n"
    await call.message.answer(msg, reply_markup=upload_media)