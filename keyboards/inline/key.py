from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Заказать обратный звонок", callback_data="zvonok"),
    ]
])