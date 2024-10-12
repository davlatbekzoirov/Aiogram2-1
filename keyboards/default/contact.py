from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contactru = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
    [
        KeyboardButton(text="📲 Поделиться контактом",request_contact=True)
    ]
])