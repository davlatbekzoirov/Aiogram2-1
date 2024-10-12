from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton as ib
from logging import basicConfig

basicConfig()

bot = Bot(token="Твой токен", parse_mode="HTML")
dp = Dispatcher(bot)
txt = """<b>Вы приняты в канал</b>"""

@dp.chat_join_request_handler()
async def join(request: ChatJoinRequest):
    await request.approve()
    await bot.send_message(request.from_user.id, text=txt)

@dp.message_handler(commands="start")
async def start(m: Message):
	await m.answer(f"Привет, {m.from_user.get_mention()}")

if __name__ == "__main__":
	executor.start_polling(dp)