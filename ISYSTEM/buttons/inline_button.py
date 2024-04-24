from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Instagram', callback_data='ins')
        ],
        [
            InlineKeyboardButton('Telegram', callback_data='tel')
        ],
        [
            InlineKeyboardButton('You Tube', callback_data='you')
        ],

    ]
)
