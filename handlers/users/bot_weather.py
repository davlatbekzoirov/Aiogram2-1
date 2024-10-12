import requests
from loader import dp
from data.config import API_KEY
import datetime
from aiogram import types
from states.Weather import Weather
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

# https://github.com/public-apis/public-apis - APILAR RO'YXATI
# https://rapidapi.com/ 

@dp.message_handler(Command('weather'), state=None)
async def enter_city(message: types.Message):
    await message.answer("Iltimos, shaharga kiring:")
    await Weather.city.set()

@dp.message_handler(state=Weather.city)
async def enter_time(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    await message.answer("Iltimos, sana va vaqtni kiriting (yil-oy-kun soat:minuta):")
    await Weather.next()

@dp.message_handler(state=Weather.time)
async def get_weather(message: types.Message, state: FSMContext):
    datetime_str = message.text
    try:
        chosen_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        await state.update_data(chosen_datetime=chosen_datetime)
        
        data = await state.get_data()
        city = data.get("city")

        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
        data = r.json()
        
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        
        reply_message = (
            f"{city} uchun ob-havo ma'lumoti {chosen_datetime}:\n"
            f"Harorat: {cur_weather}°C\n"
            f"Ob-havo: {weather_description}\n"
        )
        await message.reply(reply_message)
        await state.finish()
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        await message.reply("\U00002620 Ob-havo ma'lumoti topilmadi. Iltimos, yana bir bor urinib ko'ring.\U00002620")

