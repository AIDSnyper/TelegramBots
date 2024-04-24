from aiogram import executor
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from config import dp, bot
from buttons.replyb import *
from buttons.inlineb import *

points = 0
dsfs = []


@dp.message_handler(commands=['start'])
async def start(msg: Message):
    text = "Bizning Quiz Botimizga hush kelibsiz!👋"
    await msg.answer_photo(open('img/start.png', 'rb'), caption=text)
    await msg.answer("Quydagi bolimlardan birini tanglang!", reply_markup=chooise)
    global points
    points = 0


@dp.message_handler(commands=['help'])
async def hel(msg: Message):
    text = "Yordam uchun @abdumalikov39 ga murojaat qiling📞"
    await msg.answer_photo(open('img/help.jpeg', 'rb'), caption=text)


@dp.message_handler(text="Programming")
async def f(msg: Message):
    global points
    global dsfs
    await msg.answer("Savollar⬇", reply_markup=ReplyKeyboardRemove())
    await msg.answer("1) Python qachon paydo bolgan?", reply_markup=a1)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)
    points = 0
    dsfs = []

    @dp.callback_query_handler(text="a1")
    async def fm(call: CallbackQuery):
        global points
        global dsfs
        b = 'a1'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("2) Python fayllari uchun to'g'ri fayl kengaytmasi nima?", reply_markup=a2)

    @dp.callback_query_handler(text="a1-")
    async def d(call: CallbackQuery):
        global dsfs
        b = 'a1'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 1991")
            await call.message.answer("2) Python fayllari uchun to'g'ri fayl kengaytmasi nima?", reply_markup=a2)

    @dp.callback_query_handler(text="a2")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a2'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("3) Pythonda nechta DataType bor?", reply_markup=a3)

    @dp.callback_query_handler(text="a2-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a2'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: .py")
            await call.message.answer("3) Pythonda nechta DataType bor?", reply_markup=a3)

    @dp.callback_query_handler(text="a3")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a3'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("4) OOP ning nechta ustuni bor?", reply_markup=a4)

    @dp.callback_query_handler(text="a3-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a3'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 10 ta")
            await call.message.answer("4) OOP ning nechta ustuni bor?", reply_markup=a4)

    @dp.callback_query_handler(text="a4")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a4'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("5) Stringning qaysi metodi sozning oldidan bosh joyni olib tashlaydi?",
                                      reply_markup=a5)

    @dp.callback_query_handler(text="a4-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a4'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 4ta")
            await call.message.answer("5) Stringning qaysi metodi sozning oldidan bosh joyni olib tashlaydi?",
                                      reply_markup=a5)

    @dp.callback_query_handler(text="a5")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a5'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("6) Kodning javobi nechi boladi?\nx = 23\nnum = 0 if x > 10 else 11\nprint(num)",
                                      reply_markup=a6)

    @dp.callback_query_handler(text="a5-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a5'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: .strip()")
            await call.message.answer("6) Kodning javobi nechi boladi?\nx = 23\nnum = 0 if x > 10 else 11\nprint(num)",
                                      reply_markup=a6)

    @dp.callback_query_handler(text="a6")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a6'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("7) Siklni uzish uchun qaysi operator javobgar?", reply_markup=a7)

    @dp.callback_query_handler(text="a6-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a6'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 0")
            await call.message.answer("7) Siklni uzish uchun qaysi operator javobgar?", reply_markup=a7)

    @dp.callback_query_handler(text="a7")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a7'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("8) Klass yaratish uchun qanday kalit so'zdan foydalaniladi?", reply_markup=a8)

    @dp.callback_query_handler(text="a7-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a7'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: break")
            await call.message.answer("8) Klass yaratish uchun qanday kalit so'zdan foydalaniladi?", reply_markup=a8)

    @dp.callback_query_handler(text="a8")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a8'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("9) Ro‘yxat oxiriga element qo‘shish qaysi metod yordamida amalga oshiriladi?",
                                      reply_markup=a9)

    @dp.callback_query_handler(text="a8-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a8'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: class")
            await call.message.answer("9) Ro‘yxat oxiriga element qo‘shish qaysi metod yordamida amalga oshiriladi?",
                                      reply_markup=a9)

    @dp.callback_query_handler(text="a9")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a9'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("10) Listda qanday ma'lumotlar turlariga ruxsat beriladi?", reply_markup=a10)

    @dp.callback_query_handler(text="a9-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a9'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: .append()")
            await call.message.answer("10) Listda qanday ma'lumotlar turlariga ruxsat beriladi?", reply_markup=a10)

    @dp.callback_query_handler(text="a10")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a10'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("11) Qaysi biri togri?", reply_markup=a11)

    @dp.callback_query_handler(text="a10-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a10'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: Hamma turlarga")
            await call.message.answer("11) Qaysi biri togri?", reply_markup=a11)

    @dp.callback_query_handler(text="a11")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a11'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("12) Bulardan qaysi biri List?", reply_markup=a12)

    @dp.callback_query_handler(text="a11-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a11'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 2-si")
            await call.message.answer("12) Bulardan qaysi biri List?", reply_markup=a12)

    @dp.callback_query_handler(text="a12")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a12'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("13) Bulardan qaysi biri Set?", reply_markup=a13)

    @dp.callback_query_handler(text="a12-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a12'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 1-si")
            await call.message.answer("13) Bulardan qaysi biri Set?", reply_markup=a13)

    @dp.callback_query_handler(text="a13")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a13'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
        await call.message.answer("14) Bulardan qaysi biri Dictionary?", reply_markup=a14)

    @dp.callback_query_handler(text="a13-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a13'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 3-si")
            await call.message.answer("14) Bulardan qaysi biri Dictionary?", reply_markup=a14)

    @dp.callback_query_handler(text="a14")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a14'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer(
                "15) Qaysi biri ozgaruvchan, tartiblangan va dublikatlarga ruxsat berilgan royxatdir?",
                reply_markup=a15)

    @dp.callback_query_handler(text="a14-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a14'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: 1-si")
            await call.message.answer(
                "15) Qaysi biri ozgaruvchan, tartiblangan va dublikatlarga ruxsat berilgan royxatdir?", reply_markup=a15)

    @dp.callback_query_handler(text="a15")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a15'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("16) Qaysi birida dublikatlarga ruxsat berilmagan?", reply_markup=a16)

    @dp.callback_query_handler(text="a15-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a15'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: List")
            await call.message.answer("16) Qaysi birida dublikatlarga ruxsat berilmagan?", reply_markup=a16)

    @dp.callback_query_handler(text="a16")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a16'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("""17) Pythonda "Hello" - 'Hello' ga teng""", reply_markup=a17)

    @dp.callback_query_handler(text="a16-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a16'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: Setda")
            await call.message.answer("""17) Pythonda "Hello" - 'Hello' ga teng""", reply_markup=a17)

    @dp.callback_query_handler(text="a17")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a17'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("18) Kopaytirish opertori qaysi", reply_markup=a18)

    @dp.callback_query_handler(text="a17-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a17'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: True")
            await call.message.answer("18) Kopaytirish opertori qaysi", reply_markup=a18)

    @dp.callback_query_handler(text="a18")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a18'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("19) Qoldiqli bolish operatori qaysi?", reply_markup=a19)

    @dp.callback_query_handler(text="a18-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a18'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: *")
            await call.message.answer("19) Qoldiqli bolish operatori qaysi?", reply_markup=a19)

    @dp.callback_query_handler(text="a19")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a19'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            await call.message.answer("20) Stiring yoki listning uzunligini qaysi metod yordamida bilsa boladi?",
                                      reply_markup=a20)

    @dp.callback_query_handler(text="a19-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a19'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: %")
            await call.message.answer("20) Stiring yoki listning uzunligini qaysi metod yordamida bilsa boladi?",
                                      reply_markup=a20)

    @dp.callback_query_handler(text="a20")
    async def s(call: CallbackQuery):
        global points
        global dsfs
        b = 'a20'
        if b not in dsfs:
            points += 1
            dsfs.append(b)
            g = 100 / 20 * points
            await call.message.answer(f"Umumiy savollar❓: 20ta\nTogri ✅ : {points}ta\nXato ❌ : {20 - points}ta\nFoiz: {g}%",
                                      reply_markup=end)

    @dp.callback_query_handler(text="a20-")
    async def s(call: CallbackQuery):
        global dsfs
        b = 'a20'
        if b not in dsfs:
            dsfs.append(b)
            await call.message.answer("Togri javob: .len()")
            g = 100 / 20 * points
            await call.message.answer(f"Umumiy savollar❓: 20ta\nTogri ✅ : {points}ta\nXato ❌ : {20 - points}ta\nFoiz: {g}%",
                                      reply_markup=end)


@dp.message_handler(text="Bosh menu")
async def df(msg: Message):
    await msg.answer(f"Siz bosh menuga qaytdingiz", reply_markup=chooise)


@dp.message_handler(text="Kitoblar")
async def books(msg: Message):
    await msg.answer("Quyidagi kitoblardan birini tanglang📚", reply_markup=bookss)
    await msg.answer("Bosh menuga qaytish uchun pastagi knopkani bosing⬇", reply_markup=end)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 2)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 1)


@dp.callback_query_handler(text="1")
async def book(call: CallbackQuery):
    await call.message.answer_document(open('books/daydi qizning daftari.pdf', 'rb'))


@dp.callback_query_handler(text="2")
async def book(call: CallbackQuery):
    await call.message.answer_document(open('books/gafur_gulom_shum_bola_qissa.pdf', 'rb'))


@dp.callback_query_handler(text="3")
async def book(call: CallbackQuery):
    await call.message.answer_document(open('books/ikki_eshik_orasi.pdf', 'rb'))


@dp.callback_query_handler(text="4")
async def book(call: CallbackQuery):
    await call.message.answer_document(open('books/Oq kema. Chingiz Aytmatov.pdf', 'rb'))


@dp.callback_query_handler(text="5")
async def book(call: CallbackQuery):
    await call.message.answer_document(open('books/sariq_devni_minib_roman.pdf', 'rb'))


@dp.callback_query_handler(text="6")
async def book(call: CallbackQuery):
    await call.message.answer_document(open('books/Ufq. Said A..pdf', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
