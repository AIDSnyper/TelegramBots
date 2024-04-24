from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton('Shaharlar')]],
    resize_keyboard=True)

menu_button = ReplyKeyboardMarkup(
    keyboard=[[
            KeyboardButton('Toshkent'),
            KeyboardButton('Andijon'),
            KeyboardButton('Samarqand'),
            KeyboardButton('Buxoro')],

         [KeyboardButton('Namangan'),
         KeyboardButton("Farg'ona"),
         KeyboardButton("Jizzax"),
         KeyboardButton("Xorazm")],

         [KeyboardButton('ORQAGA'),
         KeyboardButton('BOSH MENU')]],
         resize_keyboard=True)
