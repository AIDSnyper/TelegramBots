from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Click!', callback_data='click')
        ]
    ]
)


menu_btn1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3'),
            InlineKeyboardButton(text='4', callback_data='4'),
        ],
        [
            InlineKeyboardButton(text='❌', callback_data='x'),
            InlineKeyboardButton(text='➡️', callback_data='next1'),
        ]
    ]
)

menu_btn2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='5'),
            InlineKeyboardButton(text='2', callback_data='6'),
            InlineKeyboardButton(text='3', callback_data='7'),
            InlineKeyboardButton(text='4', callback_data='8'),
        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='back2'),
            InlineKeyboardButton(text='❌', callback_data='x'),
            InlineKeyboardButton(text='➡️', callback_data='next2'),
        ]
    ]
)

menu_btn3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='9'),
            InlineKeyboardButton(text='2', callback_data='10'),
            InlineKeyboardButton(text='3', callback_data='11'),
            InlineKeyboardButton(text='4', callback_data='12'),
        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='back3'),
            InlineKeyboardButton(text='❌', callback_data='x'),
        ]
    ]
)