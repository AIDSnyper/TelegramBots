from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Kurslar'),
        ],
        [
            KeyboardButton('Biz Haqimizda'),
        ]
    ], resize_keyboard=True
)

kurslar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Foundation")
        ],
        [
            KeyboardButton("Proffesional")
        ],
        [
            KeyboardButton("Orqaga")
        ]
    ], resize_keyboard=True
)



found = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Python'),
            KeyboardButton('Java'),
        ],
        [
            KeyboardButton('Back')
        ]
    ], resize_keyboard=True
)

proff = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Python Backend'),
            KeyboardButton('Java Backend'),
        ],
        [
            KeyboardButton('Back')
        ]
    ], resize_keyboard=True
)