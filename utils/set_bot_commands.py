from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Старт бота"),
            types.BotCommand("help", "Помошь"),
            types.BotCommand("new", "Заказать новый альбом"),
            types.BotCommand("about", "О доставке, печати и ценах"),
            types.BotCommand("orders", "Отслеживание заказов"),
        ]
    )
