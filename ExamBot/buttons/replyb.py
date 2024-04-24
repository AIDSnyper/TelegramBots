from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


chooise = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Programming"),
            KeyboardButton("Kitoblar"),
        ]
    ], resize_keyboard=True
)

end = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Bosh menu"),
        ]
    ], resize_keyboard=True
)
