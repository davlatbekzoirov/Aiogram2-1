from aiogram import executor
from loader import *
# import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.planning import *
import traceback

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)

    try:db.create_table_users()
    except Exception as e:pass#print(e)
    try:weather.create_table_weather()
    except Exception as e:pass#print(e)

    for user_id, (city, time) in user_preferences.items():
        asyncio.create_task(send_daily_weather_updates(city, time))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    print("Traceback (most recent call last):")
    for line in traceback.format_stack(limit=5):
        print(line.strip())
