from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

shaharlar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Toshkent', callback_data='tosh'),
            InlineKeyboardButton(text='Andijon', callback_data='and'),
            InlineKeyboardButton(text='Samarqand', callback_data='sam'),
            InlineKeyboardButton(text='Buxoro', callback_data='bu'),
        ],
        [
            InlineKeyboardButton(text='Namangan', callback_data='nam'),
            InlineKeyboardButton(text="Farg'ona", callback_data='far'),
            InlineKeyboardButton(text='Jizzax', callback_data='jiz'),
            InlineKeyboardButton(text='Xorazm', callback_data='xor'),
        ]
    ],
    row_width=3
)