import os
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from pytube import YouTube

BOT_TOKEN = '6393229010:AAEApExZJu1YAcjJHFESO8da-G8SuuvheC4'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: Message):
    await msg.answer("Hello! Send me a YouTube video link, and I'll download it for you.")


@dp.message_handler()
async def message(msg: Message):
    url = msg.text
    await msg.answer("Start downloading")
    await download(url, msg)


async def download(url, msg):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{msg.chat.id}', f'{msg.chat.id}_{yt.title}')
    with open(f'{msg.chat.id}/{msg.chat.id}_{yt.title}', 'rb') as video:
        await msg.answer_video(video)
        os.remove(f'{msg.chat.id}/{msg.chat.id}_{yt.title}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
