from aiogram import executor
from aiogram.types import Message, ReplyKeyboardRemove
from config import dp
from my_button import typebook, badiy, detektiv, roman


@dp.message_handler(commands=['start'])
async def start(msg: Message):
    await msg.answer("Bizning kutubxona botimizga hush kelibsiz!", reply_markup=typebook)


@dp.message_handler(commands=['help'])
async def hel(msg: Message):
    await msg.answer("Yordam uchun +998(95) 355-39-88 ga murojat qiling!")


@dp.message_handler(text="Badiy")
async def back(msg: Message):
    await msg.answer("Kitobni tanglang", reply_markup=badiy)


@dp.message_handler(text="Roman")
async def back(msg: Message):
    await msg.answer("Kitobni tanglang", reply_markup=roman)


@dp.message_handler(text="Detektiv")
async def back(msg: Message):
    await msg.answer("Kitobni tanglang", reply_markup=detektiv)


@dp.message_handler(text="Otkan Kunlar")
async def back(msg: Message):
    await msg.answer("https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/a_qodiriyt_utgan_kunlar_namdu_uz.pdf")


@dp.message_handler(text="Dunyoning Ishlari")
async def back(msg: Message):
    await msg.answer("https://library.samdu.uz/files/f229f7ed2e8f42677ceb9ddb16a80b18_Dunyoning%20ishlari.pdf")


@dp.message_handler(text="Oq Kema")
async def back(msg: Message):
    await msg.answer("https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/Oq%20kema.%20Chingiz%20Aytmatov.pdf")


@dp.message_handler(text="Ufq")
async def back(msg: Message):
    await msg.answer("https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/Ufq.%20Said%20A..pdf")


@dp.message_handler(text="Sariq Devni Minib")
async def back(msg: Message):
    await msg.answer("https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/Sariq%20devni%20minib.pdf")


@dp.message_handler(text="Daydi Qizning Daftari")
async def back(msg: Message):
    await msg.answer("http://library.navoiy-uni.uz/files/daydi%20qizning%20daftari.pdf")


@dp.message_handler(text="Qaytganimda Uyda Bol")
async def back(msg: Message):
    await msg.answer(
        "https://library.samdu.uz/files/a578cff7c646046c4a076d01a8b21f1b_Qaytganimda%20uyda%20bo%E2%80%99l%20%20%20.pdf")


@dp.message_handler(text="Mafiya Sardori")
async def back(msg: Message):
    await msg.answer(
        "https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/%D0%9D%D1%83%D1%80%D0%B8%D0%B4%D0%B4%D0%B8%D0%BD%20%D0%98%D1%81%D0%BC%D0%BE%D0%B8%D0%BB%D0%BE%D0%B2.%20%D0%9C%D0%B0%D1%84%D0%B8%D1%8F%20%D1%81%D0%B0%D1%80%D0%B4%D0%B0%D1%80%D0%B8%203.pdf")


@dp.message_handler(text="Qaytganimda Uyda Bol")
async def back(msg: Message):
    await msg.answer(
        "https://library.samdu.uz/files/a578cff7c646046c4a076d01a8b21f1b_Qaytganimda%20uyda%20bo%E2%80%99l%20%20%20.pdf")


@dp.message_handler(text="Olimga Mahkum Qilinganlar")
async def back(msg: Message):
    await msg.answer(
        "https://kitobsevar.uz/kxpv/xrpt_u1zgu5dnca0t50sfh9obe0y3igfoemn1cc7x8ab0aat6abbharjfp881edfipt9sx6fu7gt7hd3.pdf")


@dp.message_handler(text="Iblis Saltanati")
async def back(msg: Message):
    await msg.answer("http://library.dtpi.uz/02661d55-3b35-490c-8a80-2b8d1314bbe5#page/4")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
