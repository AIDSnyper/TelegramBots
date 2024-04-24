import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery
from mybuttun import start_button, menu_button
from inline_button import shaharlar_button

API_TOKEN = '6286627706:AAEek15e5dgu98AwubNhrU8hYfhHXNC0xyk'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f'Salom {message.from_user.full_name}, Botimizga hush kelibsiz👋', reply_markup=start_button)


@dp.message_handler(commands=['help'])
async def help(message: Message):
    await message.answer(f'{message.from_user.full_name}, Yordam uchun +998 91 234-56-78 ga murojaat qiling🔍')


@dp.message_handler(text='Shaharlar')
async def menu(message: Message):
    await message.reply("O'zingizga kerakli viloyatni tanlang", reply_markup=shaharlar_button)


@dp.callback_query_handler(text='tosh')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Toshkent"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='and')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Andijon"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='sam')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Samarqand"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='bu')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Buxoro"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='nam')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Namangan"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='far')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Farg'ona"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='Jizzax')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Jizzax"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None


@dp.callback_query_handler(text='xor')
async def city(call: CallbackQuery):
    url = f"https://islomapi.uz/api/present/day?region=Xorazm"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        await call.message.answer(data['times'])
    else:
        return None
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)













