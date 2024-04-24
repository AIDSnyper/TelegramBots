from aiogram import executor
from aiogram.types import Message, ReplyKeyboardRemove
from config import dp
from my_buttons import show, country
import requests


@dp.message_handler(commands=['start'])
async def start(msg: Message):
    await msg.answer(f'{msg.from_user.full_name}, bizning namoz vaqtlari botiga hush kelibsiz', reply_markup=show)


@dp.message_handler(commands=['help'])
async def hel(msg: Message):
    await msg.answer('Yordam uchun +998(95) 355-39-88 ga murojat qiling!')


@dp.message_handler(text='Namoz Vaqtlarini Korish')
async def menu(message: Message):
    await message.answer('O\'zingizga kerakli bo\'limni tanlang', reply_markup=country)


@dp.message_handler(text='Toshkent')
async def toshkent(message: Message):
    a = requests.get('https://islomapi.uz/api/present/day?region=Toshkent')
    a = a.json()
    for i in a['times'].items():
        await message.answer(str(i))


@dp.message_handler(text='Andijon')
async def andijon(message: Message):
    a = requests.get('https://islomapi.uz/api/present/day?region=Andijon')
    a = a.json()
    await message.answer(a['times'])


@dp.message_handler(text='Xiva')
async def xiva(message: Message):
    a = requests.get("https://islomapi.uz/api/present/day?region=Xiva")
    a = a.json()
    for i in a['times'].items():
        await message.answer(str(i))


@dp.message_handler(text='Samarqand')
async def samar(message: Message):
    a = requests.get('https://islomapi.uz/api/present/day?region=Samarqand')
    a = a.json()
    for i in a['times'].items():
        await message.answer(str(i))


@dp.message_handler(text='Namangan')
async def namangan(message: Message):
    a = requests.get('https://islomapi.uz/api/present/day?region=Namangan')
    a = a.json()
    for i in a['times'].items():
        await message.answer(str(i))


@dp.message_handler(text='Guliston')
async def guliston(message: Message):
    a = requests.get('https://islomapi.uz/api/present/day?region=Guliston')
    a = a.json()
    for i in a['times'].items():
        await message.answer(str(i))

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
