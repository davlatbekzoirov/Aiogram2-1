from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.types import Message, CallbackQuery, ContentType
from keyboards.inline.zabrat_skidku import zabrat_skidku

@dp.message_handler(commands = "about")
async def bot_start(message: types.Message):
    album = types.MediaGroup()
    photo_id_1 = "AgACAgIAAxkBAAIBdWV3RUgVhRq4c6kzvlZmlF5KoiWJAAIF2jEborTAS4YPQw0_b1QnAQADAgADeQADMwQ"
    photo_id_2 = "AgACAgIAAxkBAAIBd2V3RXaaEZm7Q_EzmXrzVJflWOYAAwfaMRuitMBLjmxwltQ6zwsBAAMCAAN5AAMzBA"
    photo_id_3 = "AgACAgIAAxkBAAIBeWV3RYckmazB3jcyy4p_4gl_C8sCAAIJ2jEborTAS5JCvrYb6HAxAQADAgADeQADMwQ"
    photo_id_4 = "AgACAgIAAxkBAAIBe2V3RcN0j-7gSY9rz2Da6yUYw1B3AAIK2jEborTAS5J8ah-sypgQAQADAgADeQADMwQ"
    photo_id_5 = "AgACAgIAAxkBAAIBfWV3RdYwWbsdNds-tZbZuBfo-xC6AAIL2jEborTAS08W_GPLQva-AQADAgADeQADMwQ"
    photo_id_6 = "AgACAgIAAxkBAAIBf2V3ReoY3RUf7iBt6Ze39Neeyh6QAAIO2jEborTASy9UBje8vUxiAQADAgADeQADMwQ"
    album.attach_photo(photo=photo_id_1)
    album.attach_photo(photo=photo_id_2)
    album.attach_photo(photo=photo_id_3)
    album.attach_photo(photo=photo_id_4)
    album.attach_photo(photo=photo_id_5)
    album.attach_photo(photo=photo_id_6)
    await message.reply_media_group(media=album)
    await bot.send_message(chat_id=message.from_user.id, text="""
☝️ Это фотки наших фотокниг. Если нужно увидеть больше фоток, <a href='https://gallery.kindbot.me/kind_albums_examples'>переходи по этой ссылке</a>.

📱 Формат альбома - 20x20 см, он достаточно большой. Причем, я сам подгоню фото под требуемые размеры, тебе нужно только их прислать                           

💌  Доставка - в любую точку России за 300 рублей. Доставляем в очень прочных коробочках в ближайший к адресу получателя пункт выдачи заказов Boxberry. Если Boxberry в городе нет или он далеко - то в ближайшее почтовое отделение.
                           
<b>С ценами тоже все просто:</b>

🖼  Обычно я печатаю фотокнигу по цене 160 руб за 1 страницу. <u>Но прямо сейчас доступна приятная скидка - 10%!</u> 🔥

Так что альбом на 20 страниц сейчас стоит <s>не 3200 руб</s>, <b>а 2880 руб</b>!                                                                                 
""", reply_markup=zabrat_skidku)

