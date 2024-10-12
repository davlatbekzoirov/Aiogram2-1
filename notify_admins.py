import logging

from aiogram import Dispatcher

ADMINS = '6253711491'

async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message('-1002224095877', "✅Бот запустился")
    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message('-1002224095877', "❌Бот отключён")
    except Exception as err:
        logging.exception(err)