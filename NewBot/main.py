from aiogram import executor
from aiogram.types import ReplyKeyboardRemove, Message, CallbackQuery
from config import dp




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)