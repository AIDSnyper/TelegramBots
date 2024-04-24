from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


Token = '6673555976:AAFOGrjDvLbzsXASJnLuYfWFewvoAGXq8V0'
bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())
