from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Команды бота"),
            types.BotCommand("auto_comment", "Сгенерировать текст"),
            types.BotCommand("chat_gpt", "Чат с GPT-3"),
            types.BotCommand("generate_image", "Сгенерировать изображение"),
        ]
    )
