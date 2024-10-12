import requests, datetime, asyncio, tracemalloc, sqlite3
from loader import *
from data.config import API_KEY
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.Weather import Plan
from aiogram.types import ParseMode

user_preferences = {}

tracemalloc.start()

@dp.message_handler(Command('planning'))
async def set_planning(message: types.Message):
    await message.answer("Ob-havo maʼlumotlarini olishni istagan shaharni kiriting:")
    await Plan.city.set()

@dp.message_handler(state=Plan.city)
async def enter_time(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    await message.answer("Ob-havo maʼlumotlarini olishni istagan vaqtni (soat:daqiqa) kiriting (24 soatlik formatda):")
    await Plan.next()

@dp.message_handler(state=Plan.time)
async def schedule_weather_updates(message: types.Message, state: FSMContext):
    time_str = message.text
    try:
        chosen_time = datetime.datetime.strptime(time_str, "%H:%M").time()

        data = await state.get_data()
        city = data.get("city")
        
        user_id = message.from_user.id
        user_preferences[user_id] = (city, chosen_time)

        try:
            time_str = chosen_time.strftime("%H:%M")
            weather.add_user(id=user_id, city=city, time=time_str)
            await bot.send_message(chat_id='-1002077533723',text=f"""
🆕 Yangi obi-havodan ma'lumot olishni istagan odam!
🆔 Obi-havodan ma'lumot olishni istagan odamning identifikatori: {message.from_user.id}
🌆 Obi-havodan ma'lumot olishni istagan odamning shahri: {city}
⏳ Obi-havodan ma'lumot olishni istagan odamning vaqti: {time_str}
➖➖➖➖➖➖➖➖➖➖➖
🖐Jami botdan obi-havoni so'ragan odamalar: {weather.count_weather()[0]}""")
        except sqlite3.IntegrityError as err:pass

        await message.answer(f"{city} uchun kunlik ob-havo maʼlumotlari har kuni {chosen_time.strftime('%H:%M')} da yuboriladi.")
        
        asyncio.create_task(send_daily_weather_updates(city, chosen_time))
    except ValueError:
        await message.answer("Vaqt formati noto‘g‘ri. Iltimos, vaqtni quyidagi formatda kiriting: soat: daqiqa (masalan, 14:30).")
    finally:
        await state.finish()

async def send_daily_weather_updates(city, time):
  while True:
    current_time = datetime.datetime.now().time()
    time_until_update = datetime.datetime.combine(datetime.date.today(), time) - datetime.datetime.combine(datetime.date.today(), current_time)
    if time_until_update.total_seconds() < 0:
      time_until_update += datetime.timedelta(days=1) 

    await asyncio.sleep(time_until_update.total_seconds())
    for user_id, (user_city, user_time) in user_preferences.items():
      if user_city == city and user_time == time:
        weather_info = get_current_weather(city)
        await bot.send_message(user_id, weather_info, parse_mode=ParseMode.HTML)
        time_until_update = datetime.datetime.combine(datetime.date.today(), time) - datetime.datetime.combine(datetime.date.today(), current_time)
        if time_until_update.total_seconds() < 0:
          time_until_update += datetime.timedelta(days=1)


def get_current_weather(city):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
        r.raise_for_status() 
        data = r.json()
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        return f"{city}dagi hozirgi ob-havo: {cur_weather}°C, {weather_description}"
    except requests.RequestException as e:
        print(f"Ob-havo maʼlumotlarini olishda xatolik yuz berdi: {e}")
        return "Ob-havo maʼlumotlarini olishda xatolik yuz berdi. Iltimos keyinroq qayta urinib ko'ring."
    except KeyError:
        print("Ob-havo maʼlumotlarini tahlil qilishda xatolik: kutilmagan format")
        return "Ob-havo maʼlumotlarini tahlil qilishda xatolik yuz berdi. Iltimos keyinroq qayta urinib ko'ring."