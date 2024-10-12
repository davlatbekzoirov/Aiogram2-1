from aiogram import types
import openai
from loader import dp, api

@dp.message_handler(text = '/auto_comment')
async def process_text(message: types.Message):
    await message.reply("Напишите комментарий на основе вашего текста")


async def generate_comment(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@dp.message_handler(lambda message: message.text is not None)
async def process_text(message: types.Message):
    prompt = f"Напишите комментарий на основе следующего текста: {message.text}"
    comment = generate_comment(prompt)
    await message.reply(comment)
