import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from mybuttun import start_button, menu_button
from inline_button import shaharlar_button

API_TOKEN = '5966195482:AAEYnN8o5ZL6PAJWE7FDhcCgx1QU1f0Tg-Y'
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


def get_prayer_times(city):
    url = f"https://islomapi.uz/api/present/day?region={city}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data['results']['datetime'][0]['times']
    else:
        return None


@dp.callback_query_handler(lambda query: query.data.startswith('city_'))
async def process_city_selection(callback_query: types.CallbackQuery):
    selected_city = callback_query.data.split('_')[1]
    prayer_times = get_prayer_times(selected_city)

    if prayer_times:
        response = "\n".join([f"{key}: {value}" for key, value in prayer_times.items()])
        await bot.send_message(callback_query.from_user.id, response)
    else:
        await bot.send_message(callback_query.from_user.id, "Failed to fetch prayer times for the specified city.")

    # Don't forget to answer the callback query to remove the "working" status on the button
    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
