from aiogram import types
from loader import dp, api
import openai
@dp.message_handler(commands=['generate_image'])
async def generate_text(message: types.Message):
    await message.answer("Введите текст, и я сгенерирую продолжение.")

async def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

@dp.message_handler(lambda message: message.text is not None)
async def generate_text(message: types.Message):
    await message.answer("Пожалуйста, подождите.")
    prompt = message.text
    image_url = await generate_image(prompt)
    await message.answer_photo(image_url)