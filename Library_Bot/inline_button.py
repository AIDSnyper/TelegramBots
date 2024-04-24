from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Registratsiya", callback_data='regi')
        ]
    ]
)

writer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Chingiz Aytmatov', callback_data='cha'),
            InlineKeyboardButton(text='Abdulla Qodiriy', callback_data='aq'),
        ],
        [
            InlineKeyboardButton(text='Tohir Malik', callback_data='tm'),
            InlineKeyboardButton(text='Said Ahmad', callback_data='sa'),
        ],
        [
            InlineKeyboardButton(text='Alisher Navoiy', callback_data='an'),
            InlineKeyboardButton(text='Otkir Hoshimov', callback_data='oh'),
        ]
    ],
)




start2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Davom Ettirish!', callback_data='continue')
        ]
    ]
)

cha = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Oq kema', callback_data='1'),
            InlineKeyboardButton('Qiyomat', callback_data='2'),
            InlineKeyboardButton('Jamila', callback_data='3'),
        ]
    ]
)


aq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Otgan Kunlar', callback_data='a1'),
            InlineKeyboardButton('Mexribon Chayon', callback_data='a2'),
            InlineKeyboardButton('Jinlar Bazimi', callback_data='a3'),
        ]
    ]
)

tm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Baxt Saroyi', callback_data='b1'),
            InlineKeyboardButton('Oqibat', callback_data='b2'),
            InlineKeyboardButton('Talvasa', callback_data='b3'),
        ]
    ]
)

sa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Ufq', callback_data='c1'),
            InlineKeyboardButton('Jimjitlik', callback_data='c2'),
            InlineKeyboardButton('Majnun', callback_data='c3'),
        ]
    ]
)

an = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Xamsa', callback_data='e1'),
            InlineKeyboardButton('Farhod va Shirin', callback_data='e2'),
            InlineKeyboardButton('Hayrat ul Abror', callback_data='e3'),
        ]
    ]
)

oh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Ikki Eshik Orasida', callback_data='f1'),
            InlineKeyboardButton('Dunyoni Ishlari', callback_data='f2'),
            InlineKeyboardButton('Bahor Qaytmaydi', callback_data='f3'),
        ]
    ]
)

