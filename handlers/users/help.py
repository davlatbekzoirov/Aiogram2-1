from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Команды: </b>",
            "<i>/start - Старт бота</i>",
            "<i>/help - Помошь</i>",
            "<i>/new - Заказать новый альбом</i>",
            "<i>/about - О доставке, печати и ценах</i>",
            "<i>/orders - Отслеживание заказов</i>")
    
    await message.answer("\n".join(text))