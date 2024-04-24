from aiogram import executor
from config import dp
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from buttons.reply_button import *
from buttons.inline_button import *

@dp.message_handler(commands=['start'])
async def start(msg: Message):
    text = "Assalomu alaykum ISYSTEMning telegram botiga hush kelibsiz!️"
    await msg.answer_photo(open('img/photo_2023-04-19_22-27-55.jpg', 'rb'), caption=text, reply_markup=startb)


@dp.message_handler(commands=['help'])
async def start(msg: Message):
    text = "@iSystemStudentServices ga murojaat qiling"
    await msg.answer_photo(open('img/photo_2023-04-19_22-27-55.jpg', 'rb'), caption=text)


@dp.message_handler(text='Kurslar')
async def kurs(msg: Message):
    await msg.answer('Kurslar', reply_markup=kurslar)


@dp.message_handler(text='Biz Haqimizda')
async def about(msg: Message):
    text = '📍 Bizning manzil: Mirzo Ulug\'bek tumani, Mirzo Ulug\'bek ko\'chasi 54A\n📌iSystem IT Akademmiyasi - bu Axborot Texnologiyalarini o\'qitishga ixtisoslashgan akademiya. Biz talabalarga IT sohasida yuqori natijalarga erishish mumkin bo\'lgan keng ko\'lamli kurslar va dasturlarni taklif etamiz.'
    await msg.answer(text)


@dp.message_handler(text='Orqaga')
async def r(msg: Message):
    await msg.answer("Siz bosh menuga qaytdingiz", reply_markup=startb)


@dp.message_handler(text='Foundation')
async def a(msg: Message):
    await msg.answer("Tanlang", reply_markup=found)


@dp.message_handler(text='Python')
async def w(msg: Message):
    text = """
    Kursing davomiyligi 4 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:
    
Python dasturlash tilining boshlang'ich tushunchalari; 
Python da ma’lumot turlari, o’zgaruvchilar bilan ishlash;
Ma'lumotlar strukturasini;
Funksiya, satr va massivlar bilan ishlashni
Turli xil telegram-botlarni yaratish;
Obyektga yo'naltirilgan dasturlashni o'rganasiz. 

Kurslarning narxi: 900 000 so'm."""
    await msg.answer_photo(open('img/photo_2023-08-01_17-08-16.jpg', 'rb'), caption=text)


@dp.message_handler(text='Java')
async def w(msg: Message):
    text = """
    Kursing davomiyligi 4 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:
    
Java dasturlash tilining boshlang'ich tushunchalari; 
Java da ma’lumot turlari, o’zgaruvchilar bilan ishlash;
Ma'lumotlar strukturasini;
Funksiya, satr va massivlar bilan ishlashni
Turli xil telegram-botlarni yaratish;
Obyektga yo'naltirilgan dasturlashni o'rganasiz. 

Kurslarning narxi: 900 000 so'm."""
    await msg.answer_photo(open('img/photo_2023-08-01_17-08-16.jpg', 'rb'), caption=text)


@dp.message_handler(text='Back')
async def r(msg: Message):
    await msg.answer("Siz kurslar bolimiga qaytdingiz", reply_markup=kurslar)


@dp.message_handler(text='Proffesional')
async def s(msg: Message):
    await msg.answer("Tanlang", reply_markup=proff)


@dp.message_handler(text='Java Backend')
async def b(msg: Message):
    text = """
Kursing davomiyligi 6 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

Javada ma'lumotlar ombori bilan ishlash;
Fayllarni server va databasega saqlash va olish;
Spring framework(bean, core, context) spring mvc;
Spring bootda loyiha qurish(clickup.com backend qismi);
Spring framework jpa yordamida ma'lumotlar ombori bilan ishlash;
Rest full api yoza olish;
 
Kurslarning narxi: 1 300 000 so'm."""
    await msg.answer_photo(open('img/photo_2023-08-01_16-56-46.jpg', 'rb'), caption=text)


@dp.message_handler(text='Python Backend')
async def b(msg: Message):
    text = """
Kursing davomiyligi 6 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

Internet infrastrukturasi protokollar haqida tushuncha;
Sof SQL bilan ishlash va murakkab so'rovlarni optimallashtirish;
Fayllarni server va databasega saqlash va olish;
Django web framework arxitekturasi ishlash mexanizmi;
API ishlab chiqish, uchinchi tomon xizmatlari bilan integratsiya;
Dokumentatsiya yaratish va undan foydalansh;
Rest full api yoza olish;
Konteynerlash texnologiyalari, Deploy qilish;
 
Kurslarning narxi: 1 300 000 so'm."""
    await msg.answer_photo(open('img/photo_2023-08-01_16-56-53.jpg', 'rb'), caption=text)



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)