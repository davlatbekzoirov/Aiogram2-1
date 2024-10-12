import logging, random, string
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from notify_admins import on_shutdown_notify, on_startup_notify
from set_bot_commands import set_default_commands
from db import Database

REFERRAL_BASE_URL = 'https://t.me/davlatbekvkmbot?start=' 
API_TOKEN = '2079588730:AAG1qy76ynpN0YI8CgEnYEs7UrJRQSUwY5E'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
db = Database('main.db')
try:
    db.create_table_users()
    db.create_table_messages()
except:pass

user_data = {}
referral_data = {}
messages_data = {}

# def generate_referral_code(length=6):
#     """Generate a random referral code."""
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     args = message.get_args()
#     user_id = message.from_user.id

#     if args:
#         referral_code = args.strip()
#         db.add_user(user_id, referral_code=referral_code)
# #             user_bio = message.from_user.bio if message.from_user.bio else "Нет биографии"
# #             new_user_message = f"""🆕 Новый пользователь!
# # 🆔 Идентификатор пользователя: {user_id}
# # 📛 Пользователь: {message.from_user.full_name}
# # 🌐 Имя пользователя: @{message.from_user.username if message.from_user.username else "Нет"}
# # 📍 Биография пользователя: {user_bio}
# # ➖➖➖➖➖➖➖➖➖➖➖
# # 🖐Итого: {db.count_users()[0]}"""

# #             await bot.send_message('-1002224095877', new_user_message, parse_mode='HTML')
#         if referral_code in referral_data:
#             referrer_id = referral_data[referral_code]
#             welcome_message = (
#                 "🚀 Здесь можно отправить анонимное сообщение человеку, который опубликовал эту ссылку.\n\n"
#                 "Напишите сюда всё, что хотите ему передать, и через несколько секунд он получит ваше сообщение, но не будет знать от кого.\n\n"
#                 "Отправить можно фото, видео, 💬 текст, 🔊 голосовые, 📷видеосообщения (кружки), а также стикеры.\n\n"
#                 "⚠️ Это полностью анонимно!"
#                 f"<a href={referrer_id}> </a>"
#             )
#             await message.reply(welcome_message, parse_mode='html')
#             messages_data[user_id] = {'referred_by': referrer_id, 'messages': []}
#         else:
#             await message.reply("Неверный реферальный код. Добро пожаловать!")
#     else:
#         referral_code = generate_referral_code()
#         referral_data[referral_code] = user_id
#         referral_link = f"{REFERRAL_BASE_URL}{referral_code}"
#         user_data[user_id] = {'referral_code': referral_code, 'referral_link': referral_link}
#         intro_message = (
#             "🚀 Начни получать анонимные сообщения прямо сейчас!\n\n"
#             "<i>Твоя личная ссылка:</i>\n"
#             f"👉{referral_link}\n\n"
#             "Размести эту ссылку ☝️ в своём профиле Telegram/Instagram/TikTok или других соц сетях, чтобы начать получать сообщения 💬"
#         )
#         await message.reply(intro_message, parse_mode='html')

# @dp.message_handler(commands=['help'])
# async def help(message: types.Message):
#     await message.reply('start - Запустить бота\nhelp-Помощь\nreply-ОТправить анонимное сообшение через id-человека')

# @dp.message_handler(commands=['reply'])
# async def reply_to_message(message: types.Message):
#     user_id = message.from_user.id
#     args = message.get_args().split(' ', 1)

#     if len(args) < 2:
#         await message.reply("Укажите идентификатор пользователя и свой ответ. Пример: /reply <user_id> <ваш_ответ>")
#         return

#     target_user_id, reply_text = args[0], args[1]
    
#     if not target_user_id.isdigit():
#         await message.reply("Неверный идентификатор пользователя.")
#         return

#     target_user_id = int(target_user_id)

#     if target_user_id in messages_data and messages_data[target_user_id]['referred_by'] == user_id:
#         await bot.send_message(target_user_id, f"Ответ от вашего реферера: {reply_text}")
#         await message.reply("Твой ответ успешно отправлен 😺")
#     else:
#         await message.reply("Вы не уполномочены отвечать этому пользователю или неверный идентификатор пользователя..")

# @dp.message_handler()
# async def handle_anonymous_message(message: types.Message):
#     user_id = message.from_user.id
#     # print()
#     if message.reply_to_message:
#         try:
#             identifikator = message.reply_to_message.entities[0].user.id
#             await bot.send_message(identifikator,f"<a href='tg://user?id={message.from_user.id}'> </a> У тебя новое анонимное сообщение!:\n\n{message.text}\n\n↩️ Свайпни для ответа.",parse_mode='html')
#         except:
#             if user_id in messages_data:
#                 referrer_id = messages_data[user_id]['referred_by']
#                 messages_data[user_id]['messages'].append(message.text)
#                 await message.reply("Твой ответ успешно отправлен 😺")
#                 await bot.send_message(referrer_id, f"<a href='tg://user?id={message.from_user.id}'> </a> У тебя новое анонимное сообщение!:\n\n{message.text}\n\n↩️ Свайпни для ответа.",parse_mode='html')

#     elif user_id in messages_data: # elifni if qilib qo'yasiz
#         referrer_id = messages_data[user_id]['referred_by']
#         messages_data[user_id]['messages'].append(message.text)
#         await message.reply("Твой ответ успешно отправлен 😺")
#         await bot.send_message(referrer_id, f"<a href='tg://user?id={message.from_user.id}'> </a> У тебя новое анонимное сообщение!:\n\n{message.text}\n\n↩️ Свайпни для ответа.",parse_mode='html')
#     else:
#         await message.reply("Для отправки анонимного сообщения вам необходимо использовать реферальную ссылку...")

# async def on_startup(dispatcher):
#     await set_default_commands(dispatcher)
#     await on_startup_notify(dispatcher)

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)





def generate_referral_code(length=6):
    """Generate a random referral code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    args = message.get_args()
    user_id = message.from_user.id

    if args:
        referral_code = args.strip()
        db.add_user(user_id, referral_code)
        if referral_code in referral_data:
            referrer_id = referral_data[referral_code]
            welcome_message = (
                "🚀 Здесь можно отправить анонимное сообщение человеку, который опубликовал эту ссылку.\n\n"
                "Напишите сюда всё, что хотите ему передать, и через несколько секунд он получит ваше сообщение, но не будет знать от кого.\n\n"
                "Отправить можно фото, видео, 💬 текст, 🔊 голосовые, 📷видеосообщения (кружки), а также стикеры.\n\n"
                "⚠️ Это полностью анонимно!"
                f"<a href={referrer_id}> </a>"
            )
            await message.reply(welcome_message, parse_mode='html')
            messages_data[user_id] = {'referred_by': referrer_id, 'messages': []}
        else:
            await message.reply("Неверный реферальный код. Добро пожаловать!")
    else:
        referral_code = generate_referral_code()
        referral_data[referral_code] = user_id
        referral_link = f"{REFERRAL_BASE_URL}{referral_code}"
        user_data[user_id] = {'referral_code': referral_code, 'referral_link': referral_link}
        intro_message = (
            "🚀 Начни получать анонимные сообщения прямо сейчас!\n\n"
            "<i>Твоя личная ссылка:</i>\n"
            f"👉{referral_link}\n\n"
            "Размести эту ссылку ☝️ в своём профиле Telegram/Instagram/TikTok или других соц сетях, чтобы начать получать сообщения 💬"
        )
        await message.reply(intro_message, parse_mode='html')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('start - Запустить бота\nhelp - Помощь\nreply - Отправить анонимное сообщение через id-человека')

@dp.message_handler(commands=['reply'])
async def reply_to_message(message: types.Message):
    user_id = message.from_user.id
    args = message.get_args().split(' ', 1)

    if len(args) < 2:
        await message.reply("Укажите идентификатор пользователя и свой ответ. Пример: /reply <user_id> <ваш_ответ>")
        return

    target_user_id, reply_text = args[0], args[1]
    
    if not target_user_id.isdigit():
        await message.reply("Неверный идентификатор пользователя.")
        return

    target_user_id = int(target_user_id)

    if target_user_id in messages_data and messages_data[target_user_id]['referred_by'] == user_id:
        try:
            user_info = await bot.get_chat_member(chat_id=target_user_id, user_id=target_user_id)
            if user_info.user.is_bot:
                await message.reply("Нельзя отправить сообщение боту.")
            else:
                await bot.send_message(target_user_id, f"Ответ от вашего реферера: {reply_text}")
                await message.reply("Твой ответ успешно отправлен 😺")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            await message.reply("Ошибка при отправке сообщения.")
    else:
        await message.reply("Вы не уполномочены отвечать этому пользователю или неверный идентификатор пользователя.")

@dp.message_handler()
async def handle_anonymous_message(message: types.Message):
    user_id = message.from_user.id

    if message.reply_to_message:
        try:
            identifikator = message.reply_to_message.from_user.id
            user_info = await bot.get_chat_member(chat_id=identifikator, user_id=identifikator)
            await bot.send_message(identifikator, f"<a href='tg://user?id={user_id}'> </a> У тебя новое анонимное сообщение!:\n\n{message.text}\n\n↩️ Свайпни для ответа.", parse_mode='html')
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            if user_id in messages_data:
                referrer_id = messages_data[user_id]['referred_by']
                messages_data[user_id]['messages'].append(message.text)
                db.add_user_message(user_id, referrer_id, message.text)
                await message.reply("Твой ответ успешно отправлен 😺")
                await bot.send_message(referrer_id, f"<a href='tg://user?id={user_id}'> </a> У тебя новое анонимное сообщение!:\n\n{message.text}\n\n↩️ Свайпни для ответа.", parse_mode='html')

    elif user_id in messages_data:
        referrer_id = messages_data[user_id]['referred_by']
        messages_data[user_id]['messages'].append(message.text)
        db.add_user_message(user_id, referrer_id, message.text)
        await message.reply("Твой ответ успешно отправлен 😺")
        await bot.send_message(referrer_id, f"<a href='tg://user?id={user_id}'> </a> У тебя новое анонимное сообщение!:\n\n{message.text}\n\n↩️ Свайпни для ответа.", parse_mode='html')
    else:
        await message.reply("Для отправки анонимного сообщения вам необходимо использовать реферальную ссылку...")

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)