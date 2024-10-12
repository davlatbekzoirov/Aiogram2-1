import logging
import moviepy.editor as mp
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['video'])
async def make_video(message: types.Message):
    file_id = message.video.file_id
    file = await bot.get_file(file_id)
    path = f"{message.from_user.id}video.mp4"
    await bot.download_file(file.file_path, path)
    clip = mp.VideoFileClip(path)
    clip = clip.resize((300, 300))
    path_resized = f'{message.from_user.id}resized.mp4'
    clip.write_videofile(path_resized)
    await message.answer_video_note(open(path_resized, "rb"))


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
