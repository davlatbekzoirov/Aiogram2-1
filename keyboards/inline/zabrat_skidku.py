from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



zabrat_skidku = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Забрать скидку😎", callback_data="zabrat_skidku")
    ]
])
foto_album_create = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💌Создать фотокнигу!", callback_data="foto_album_create")
    ]
])

upload_media = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Отлично, давай загружать!", callback_data="upload_media")
    ]
])

refresh_bot = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔄 Оюновить отслеживаний", callback_data="refresh_bo1")
    ],
    [
        InlineKeyboardButton(text="Вернуться к печати фотокниг", callback_data="refresh_bo2")
    ]
])
