from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "запустить бота"),
            types.BotCommand("help", "помощь"),
            types.BotCommand("new_post", "новый пост"),
        ]
    )
