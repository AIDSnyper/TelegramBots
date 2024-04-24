from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

typebook = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Badiy"),
            KeyboardButton("Roman"),
            KeyboardButton("Detektiv"),

        ]
    ], resize_keyboard=True
)

badiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Otkan Kunlar"),
            KeyboardButton("Dunyoning Ishlari"),
            KeyboardButton("Oq Kema"),
        ],
        [
            KeyboardButton("Ufq"),
            KeyboardButton("Sariq Devni Minib"),
        ]
    ], resize_keyboard=True
)

roman = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Daydi Qizning Daftari"),
            KeyboardButton("Qaytganimda Uyda Bol"),
        ]
    ], resize_keyboard=True
)

detektiv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mafiya Sardori"),
            KeyboardButton("Olimga Mahkum Qilinganlar"),
            KeyboardButton("Iblis Saltanati"),
        ]
    ], resize_keyboard=True
)