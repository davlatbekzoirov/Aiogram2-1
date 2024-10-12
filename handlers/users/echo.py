from aiogram import types

from loader import dp

# Wiki bot
@dp.message_handler()
async def sendWiki(message: types.Message):
    await message.answer()
