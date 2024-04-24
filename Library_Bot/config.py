from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '6521101183:AAGRg42SD9Wl2G45L8H39keQgJNj6BvTDzo'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
