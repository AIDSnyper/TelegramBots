from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bookss = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Daydi Qizning Daftari", callback_data='1'),
            InlineKeyboardButton(text="Shum Bola", callback_data='2'),
        ],
        [
            InlineKeyboardButton(text="Ikki Eshik Orasida", callback_data='3'),
            InlineKeyboardButton(text="Oq Kema", callback_data='4'),
        ],
        [
            InlineKeyboardButton(text="Sariq Devni Minib", callback_data='5'),
            InlineKeyboardButton(text="Ufq", callback_data='6'),
        ],
    ]
)


a1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1991", callback_data='a1'),
            InlineKeyboardButton(text="2001", callback_data='a1-'),
            InlineKeyboardButton(text="1989", callback_data='a1-'),
        ]
    ]
)

a2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=".python", callback_data='a2-'),
            InlineKeyboardButton(text=".js", callback_data='a2-'),
            InlineKeyboardButton(text=".py", callback_data='a2'),
        ]
    ]
)

a3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="8", callback_data='a3-'),
            InlineKeyboardButton(text="4", callback_data='a3-'),
            InlineKeyboardButton(text="10", callback_data='a3'),
        ]
    ]
)

a4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="3", callback_data='a4-'),
            InlineKeyboardButton(text="5", callback_data='a4-'),
            InlineKeyboardButton(text="4", callback_data='a4'),
        ]
    ]
)

a5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=".join()", callback_data='a5-'),
            InlineKeyboardButton(text=".strip()", callback_data='a5'),
            InlineKeyboardButton(text=".lstrip()", callback_data='a5-'),
        ]
    ]
)

a6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="11", callback_data='a6-'),
            InlineKeyboardButton(text="0", callback_data='a6'),
            InlineKeyboardButton(text="23", callback_data='a6-'),
        ]
    ]
)

a7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="stop", callback_data='a7-'),
            InlineKeyboardButton(text="break", callback_data='a7'),
            InlineKeyboardButton(text="continue", callback_data='a7-'),
        ]
    ]
)

a8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="class", callback_data='a8'),
            InlineKeyboardButton(text="def", callback_data='a8-'),
            InlineKeyboardButton(text="try", callback_data='a8-'),
        ]
    ]
)

a9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=".insert()", callback_data='a9-'),
            InlineKeyboardButton(text=".index()", callback_data='a9-'),
            InlineKeyboardButton(text=".append()", callback_data='a9'),
        ]
    ]
)

a10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hamma turlarga", callback_data='a10'),
            InlineKeyboardButton(text="string va int", callback_data='a10-'),
            InlineKeyboardButton(text="float va char", callback_data='a10-'),
        ]
    ]
)

a11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="/*This is a comment*/", callback_data='a11-'),
        ],
        [
            InlineKeyboardButton(text="#This is a comment", callback_data='a11'),
        ],
        [
            InlineKeyboardButton(text="//This is a comment", callback_data='a11-'),
        ]
    ]
)

a12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="['apple', 'cherry', 'banana']", callback_data='a12'),
        ],
        [
            InlineKeyboardButton(text="('apple', 'cherry', 'banana')", callback_data='a12-'),
        ],
        [
            InlineKeyboardButton(text="{'apple', 'cherry', 'banana'}", callback_data='a12-'),
        ]
    ]
)

a13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="['apple', 'cherry', 'banana']", callback_data='a13-'),
        ],
        [
            InlineKeyboardButton(text="{'a':'apple', 'b':'cherry', 'c':'banana'}", callback_data='a13-'),
        ],
        [
            InlineKeyboardButton(text="{'apple', 'cherry', 'banana'}", callback_data='a13'),
        ]
    ]
)

a14 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="{'a':'apple', 'b':'cherry', 'c':'banana'}", callback_data='a14'),
        ],
        [
            InlineKeyboardButton(text="['apple', 'cherry', 'banana']", callback_data='a14-'),
        ],
        [
            InlineKeyboardButton(text="{'apple', 'cherry', 'banana'}", callback_data='a14-'),
        ]
    ]
)

a15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="List", callback_data='a15'),
            InlineKeyboardButton(text="Set", callback_data='a15-'),
            InlineKeyboardButton(text="Tuple", callback_data='a15-'),
        ]
    ]
)

a16 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="List", callback_data='a16-'),
            InlineKeyboardButton(text="Set", callback_data='a16'),
            InlineKeyboardButton(text="Tuple", callback_data='a16-'),
        ]
    ]
)

a17 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="True", callback_data='a17'),
            InlineKeyboardButton(text="False", callback_data='a17-'),
        ]
    ]
)

a18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="%", callback_data='a18-'),
            InlineKeyboardButton(text="*", callback_data='a18'),
            InlineKeyboardButton(text="x", callback_data='a18-'),
        ]
    ]
)

a19 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="%", callback_data='a19'),
            InlineKeyboardButton(text="*", callback_data='a19-'),
            InlineKeyboardButton(text="#", callback_data='a19-'),
        ]
    ]
)

a20 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=".len()", callback_data='a20'),
            InlineKeyboardButton(text=".index()", callback_data='a20-'),
            InlineKeyboardButton(text=".sum()", callback_data='a20-'),
        ]
    ]
)
