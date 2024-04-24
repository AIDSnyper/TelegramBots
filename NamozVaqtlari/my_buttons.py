from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

show = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Namoz Vaqtlarini Korish")
        ]
    ], resize_keyboard=True
)

country = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Toshkent'),
            KeyboardButton('Andijon'),
            KeyboardButton('Xiva'),
        ],
        [
            KeyboardButton('Samarqand'),
            KeyboardButton('Namangan'),
            KeyboardButton('Guliston'),
        ]
    ], resize_keyboard=True
)


