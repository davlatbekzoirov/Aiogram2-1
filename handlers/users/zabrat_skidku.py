import logging
from aiogram import types
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from keyboards.inline.zabrat_skidku import zabrat_skidku, foto_album_create, upload_media
from keyboards.default.send_photo import menu
from loader import dp, bot
from pathlib import Path

download_path = Path().joinpath("downloads","photos")
download_path.mkdir(parents=True, exist_ok=True)

photo_count = {}

@dp.callback_query_handler(text="zabrat_skidku")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    sticker_id = "CAACAgIAAxkBAAEK8oRld01n_YXngvZYVpuCY0bEw95VBQACHgAD6dgTKLO-IwM5OGbpMwQ"
    await bot.send_sticker(chat_id = call.message.chat.id,
                           sticker = sticker_id)
    msg = "<u>Скидка на 10% выдана. Теперь просто закажи новую фотокнигу. Скидка применится автоматически в конце заказа!</u>\n\n"
    msg += "Кстати, фотокнигу для тебя может собрать наш дизайнер. Чтобы обратиться к дизайнеру, пиши нам в <a href='https://t.me/your_kind_support'>личку</a> хочу дизайн. Мы на связи и сразу поможем!\n\n"
    msg += "А если хочешь собрать фотокнигу с помощью бота сам, жми на кнопку ниже, чтобы сделать заказ 👇"
    await call.message.answer(msg, reply_markup=foto_album_create)

@dp.callback_query_handler(text = "foto_album_create")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    video = "BAACAgIAAxkBAAICNWV3WRytoy3qE1jJU0S3DsWQz0Q6AAIrMQACre7ASYApVbKl1FS7MwQ"
    await bot.send_video(chat_id=call.message.chat.id, video=video)
    msg = "Сначала давай сделаем самое важное - загрузим фотки для фотокниги!\n\n"
    msg += "Кстати, фотокнигу для тебя может собрать наш дизайнер. Чтобы обратиться к дизайнеру, пиши нам в <a href='https://t.me/your_kind_support'>личку</a> хочу дизайн. Мы на связи и сразу поможем!\n\n"
    msg += "А если хочешь собрать фотокнигу с помощью бота сам, жми на кнопку ниже, чтобы сделать заказ 👇"
    await call.message.answer(msg, reply_markup=upload_media)

@dp.callback_query_handler(text="upload_media")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    msg = "Нажми на скрепку и прикрепи мне фото, которые ты хочешь добавить в фотокнигу!\n\n\n"
    msg += "❗️ Когда отправишь все фото, просто напиши мне: готово\n\n"
    msg += "❗️ Важно! Дождись загрузки всех фото и только потом напиши мне: готово"
    await call.message.answer(msg)

photo_count = {}

@dp.message_handler(content_types=ContentType.PHOTO)
async def handle_photos(message: types.Message):
    user_id = message.from_user.id

    if user_id not in photo_count:
        photo_count[user_id] = 1
    else:
        photo_count[user_id] += 1

    try:
        await message.photo[-1].download(destination_dir=download_path)
        if photo_count[user_id] >= 20:
            msg = f"Ты отправил {photo_count[user_id]} фото. Для фотокниги нужно не менее 20 фото (по 2 на каждом развороте). Нажми на скрепку и отправь мне еще фото, которые ты хочешь напечатать.\n\n"
            msg += "❗️ Когда отправишь все фото, просто напиши мне: готово\n\n"
            msg += f"Если думаешь, что с ботом что-то не так, напишите нам в личку: [your_kind_support](https://t.me/your_kind_support). Мы на связи и сразу поможем!"
            await message.reply(msg, reply_markup=menu)
        else:
            message_by = f"Ты отправил {photo_count[user_id]} фото. Вижу, что загружаешь фото! Когда все фото загрузятся, напишите мне: готово"
            await message.reply(message_by, reply_markup=menu)
    except Exception as e:
        msg = f"Произошла ошибка при загрузке фото: {str(e)}\n\n"
        msg += "Нажмите на скрепку и отправьте мне фото, которые вы хотите добавить в фотокнигу.\n\n"
        msg += "❗️ Когда отправите все фото, просто напишите мне: готово\n\n"
        msg += f"Если с ботом что-то не так, напишите нам в личку: [your_kind_support](https://t.me/your_kind_support). Мы на связи и сразу поможем!"
        await message.reply(msg, reply_markup=menu)

@dp.message_handler(text='Готово, я отправил все фото')
async def buy_courses(message: types.Message):
    user_id = message.from_user.id
    # callback_data = message.data
    # logging.info(f"{callback_data=}")
    logging.info(f"{message.from_user.username=}")
    msg = f"Ты отправил фото. Для фотокниги нужно не менее 20 фото (по 2 на каждом развороте)."
    msg += "❗️ Когда отправишь все фото, просто напиши мне: готово\n"
    msg += "Если думаешь, что с ботом что-то не так, напишите нам в <a href='https://t.me/your_kind_support'>личку</a>. Мы на связи и сразу поможем!"
    await message.answer(msg, reply_markup=ReplyKeyboardRemove())