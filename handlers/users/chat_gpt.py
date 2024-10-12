from aiogram import types
import openai
import requests
from bs4 import BeautifulSoup
from loader import dp, api


@dp.message_handler(commands=['chat_gpt'])
async def process_start_command(message: types.Message):
    await message.reply("Отправьте мне текст, и я ответю на твой вопрос.")

@dp.message_handler(lambda message: message.text is not None)
async def echo(message: types.Message):
    await message.reply("Пожалуйста, подождите.")

    def get_info(prompt):
        r = requests.get("https://www.google.com/search?q=" + prompt)
        data = BeautifulSoup(r.text, "html.parser").text

        custom_prompt = """
        The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n
    """


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "assistant", 
             "content": get_info(message.text)
        }]
    )

    await message.reply(response["choices"][0]["message"]["content"])
