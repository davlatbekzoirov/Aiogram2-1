from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Готово, я отправил все фото', callback_data="menu1"),
        ],
    ],
    resize_keyboard=True
)
