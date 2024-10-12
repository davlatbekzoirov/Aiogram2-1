import logging
from aiogram import types
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from keyboards.inline.zabrat_skidku import zabrat_skidku, foto_album_create, upload_media
from loader import dp, bot
from aiogram import types
@dp.message_handler(commands = "new")
async def buy_courses(message: types.Message):
    album = types.MediaGroup()
    video1 = "BAACAgIAAxkBAAICNWV3WRytoy3qE1jJU0S3DsWQz0Q6AAIrMQACre7ASYApVbKl1FS7MwQ"
    msg = "Сначала давай сделаем самое важное - загрузим фотки для фотокниги!\n"
    msg += "Размер альбома - 20*20 см. На каждом развороте - по 2 фотки. C твоей скидкой такой разворот будет стоить 288 руб  320 руб! \n"
    msg += "Необходимо загрузить от 20 до 60 фото.\n"
    msg += "Я сам создам фотокнигу, тебе надо просто скинуть фотки в пару кликов!\n"
    msg += "Если будут любые вопросы, можешь написать нам в <a href='https://t.me/your_kind_support'>личку</a>.Мы на связи и сразу поможем!\n"
    msg += "👇 Жми на кнопку ниже, чтобы загрузить фотки:\n"
    album.attach_video(video=video1)
    await message.reply_media_group(media=album)
    await message.answer(msg, reply_markup=upload_media)