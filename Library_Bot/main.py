from aiogram import executor
from aiogram.dispatcher import FSMContext
import inline_button
from config import dp
from aiogram.types import CallbackQuery, Message
from inline_button import *
from state import PersonalData


@dp.message_handler(commands=['start'])
async def start(msg: Message):
    text = "Kutubxona botimizga xush kelibsiz!"
    img = open('img/book.jpeg', 'rb')
    await msg.answer_photo(img, caption=text)
    await msg.answer('Boshlashdan avval royxatdan oting!', reply_markup=inline_button.reg)


@dp.message_handler(commands=['help'])
async def start(msg: Message):
    text = "Yordam uchun @abdumalikov39 ga murojaat qiling!"
    img = open('img/help.jpeg', 'rb')
    await msg.answer_photo(img, caption=text)


@dp.callback_query_handler(text='regi')
async def reg(call: CallbackQuery):
    await call.message.answer('Ismingizni kiriting...')
    await PersonalData.name.set()


@dp.message_handler(state=PersonalData.name)
async def names(msg: Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {
            'name': name
        }
    )
    await msg.answer('Familiyangizni kiriting...')
    await PersonalData.next()


@dp.message_handler(state=PersonalData.lname)
async def names(msg: Message, state: FSMContext):
    lname = msg.text
    await state.update_data(
        {
            'lname': lname
        }
    )
    await msg.answer('Emailni kiriting...')
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def emails(msg: Message, state: FSMContext):
    email = msg.text
    await state.update_data(email=email)
    await msg.answer('Telefon raqamni kiriting...')
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phone)
async def phones(msg: Message, state: FSMContext):
    phone = msg.text
    await state.update_data(phone=phone)
    data = await state.get_data()
    name = data.get('name')
    lname = data.get('lname')
    email = data.get('email')
    phone = data.get('phone')
    msgs = 'Quyidagi ma\'lumotlar qabul qilindi:\n'
    msgs += f'Ism: {name}\n'
    msgs += f'Familiya: {lname}\n'
    msgs += f'Email: {email}\n'
    msgs += f'Phone: {phone}\n'
    await msg.answer(msgs, reply_markup=start2)
    await state.finish()


@dp.callback_query_handler(text='continue')
async def con(call: CallbackQuery):
    await call.message.answer("Kitob muallifini tanglang!", reply_markup=writer)


@dp.callback_query_handler(text='cha')
async def m(call: CallbackQuery):
    text = 'Chingiz To‘raqulovich Aytmatov XX asr qirg‘iz adabiyotining eng iste’dodli va jahonga tanilgan yirik namoyandalaridan biri bo‘lib, u 1928 yil 12 dekabrda Qirg‘izistonning Talas vodiysidagi Shakar ovulida tug‘ilgan.'
    text2 = 'Chingiz Aytmatovning taniqli kitoblari'
    await call.message.answer(text)
    await call.message.answer(text2, reply_markup=cha)


@dp.callback_query_handler(text='aq')
async def m(call: CallbackQuery):
    text = 'Abdulla Qodiriy (Julqunboy)- yozuvchi, shoir, tarjimon, dramaturg, XX asr o‘zbek adabiyotining ulkan namoyondalaridan biri, o‘zbek romanchiligi asoschisi, 1894 yil 10-aprelda Toshkent shahrining Eskijo‘va mahallasida tavallud topgan.'
    text2 = 'Abdulla Qodiriyning taniqli kitoblari'
    await call.message.answer(text)
    await call.message.answer(text2, reply_markup=aq)


@dp.callback_query_handler(text='tm')
async def m(call: CallbackQuery):
    text = 'Tohir Malik (Hobilov Tohir Abdumalikovich) 1946 yil 27 dekabrda Toshkent shahrida tug‘ilgan. O‘zbekiston xalq yozuvchisi (2000). O‘zbek fantastikasining asoschilaridan biri.'
    text2 = 'Tohir Malikning taniqli kitoblari'
    await call.message.answer(text)
    await call.message.answer(text2, reply_markup=tm)


@dp.callback_query_handler(text='sa')
async def m(call: CallbackQuery):
    text = 'Said Ahmad 1920-yil 10-iyunda Toshkent shahri “Samarqand darvoza” mahallasida o‘z davrining obro‘li insonlaridan bo‘lgan Husanxo‘ja Dadaxo‘jayev oilasida dunyoga kelgan.'
    text2 = 'Said Ahmadovning taniqli kitoblari'
    await call.message.answer(text)
    await call.message.answer(text2, reply_markup=sa)


@dp.callback_query_handler(text='an')
async def m(call: CallbackQuery):
    text = 'Alisher Navoiy 1441-yil 9-fevral kuni Xuroson davlatining poytaxti — hozirgi Afg‘oniston hududidagi Hirot shahrining Bog‘i Davlatxona mavzesida tug‘ildi.'
    text2 = 'Alisher Navoiyning taniqli kitoblari'
    await call.message.answer(text)
    await call.message.answer(text2, reply_markup=an)


@dp.callback_query_handler(text='oh')
async def m(call: CallbackQuery):
    text = 'O‘zbekiston xalq yozuvchisi va jamiyat arbobi O‘tkir Hoshimovdir (1941 - 2013). U qariyb qirq yildan buyon o‘zining ajoyib publitsistik maqolalari, xikoya, qissa va romanlari bilan adabiyotimiz taraqqiyotiga munosib ulush qo‘shib keldi.'
    text2 = 'Otkir Hoshimovning taniqli kitoblari'
    await call.message.answer(text)
    await call.message.answer(text2, reply_markup=oh)


@dp.callback_query_handler(text='1')
async def n(call: CallbackQuery):
    await call.message.answer('https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/Oq%20kema.%20Chingiz%20Aytmatov.pdf')


@dp.callback_query_handler(text='2')
async def n(call: CallbackQuery):
    await call.message.answer('http://library.navoiy-uni.uz/files/chingiz%20aytmatov%20-qiyomat%20roman.pdf')


@dp.callback_query_handler(text='3')
async def n(call: CallbackQuery):
    await call.message.answer('https://n.ziyouz.com/books/jahon_nasri/Chingiz%20Aytmatov.%20Jamila%20(qissa).pdf')

@dp.callback_query_handler(text='a1')
async def n(call: CallbackQuery):
    await call.message.answer('https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/a_qodiriyt_utgan_kunlar_namdu_uz.pdf')


@dp.callback_query_handler(text='a2')
async def n(call: CallbackQuery):
    await call.message.answer('http://library.navoiy-uni.uz/files/abdulla%20qodiriy_%20mehrobdan%20chayon.pdf')


@dp.callback_query_handler(text='a3')
async def n(call: CallbackQuery):
    await call.message.answer('http://library.navoiy-uni.uz/files/abdulla%20qodiriy.%20jinlar%20bazmi%20(hikoyalar).pdf')


@dp.callback_query_handler(text='b1')
async def n(call: CallbackQuery):
    await call.message.answer('https://www.ziyouz.com/portal-haqida/xarita/ibratli-hikoyatlar/baxt-saroyi')


@dp.callback_query_handler(text='b2')
async def n(call: CallbackQuery):

    await call.message.answer('https://e-library.namdu.uz/81%20%D0%A2%D0%B8%D0%BB%D1%88%D1%83%D0%BD%D0%BE%D1%81%D0%BB%D0%B8%D0%BA/Turkiy%20xalqlar%20adabiyoti%20tarixi.%20Suyarova%20A.pdf')


@dp.callback_query_handler(text='b3')
async def n(call: CallbackQuery):
    await call.message.answer('https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/%D0%A2%D0%B0%D1%85%D0%B8%D1%80%20%D0%9C%D0%B0%D0%BB%D0%B8%D0%BA.%20%D0%A2%D0%B0%D0%BB%D0%B2%D0%B0%D1%81%D0%B0.%20%D0%9E%D0%B7%D0%BE%D0%B4%20%D0%98%D0%BD%D1%81%D0%BE%D0%BD%20%D1%85%D0%B0%D0%BA%D0%B8%D0%B4%D0%B0%20%D0%BA%D1%83%D1%88%D0%B8%D0%BA.pdf')


@dp.callback_query_handler(text='c1')
async def n(call: CallbackQuery):
    await call.message.answer('https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/Ufq.%20Said%20A..pdf')


@dp.callback_query_handler(text='c2')
async def n(call: CallbackQuery):
    await call.message.answer('http://qr.natlib.uz/file/read/05db0a14-f7d7-47bc-9ae8-6f53543ecc01.pdf')


@dp.callback_query_handler(text='c3')
async def n(call: CallbackQuery):
    await call.message.answer('http://kutubxonachi.uz/media/books/korakuz-mazhnun_kutubxonachi.uz.pdf')


@dp.callback_query_handler(text='e1')
async def n(call: CallbackQuery):
    await call.message.answer('https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/Xamsa.%20Alisher%20Navoiy.pdf')


@dp.callback_query_handler(text='e2')
async def n(call: CallbackQuery):
    await call.message.answer('https://lib.fbtuit.uz/assets/files/Alisher-Navoiy.FarhodvaShirin.pdf')


@dp.callback_query_handler(text='e3')
async def n(call: CallbackQuery):
    await call.message.answer('https://n.ziyouz.com/books/alisher_navoiy_asarlari/Alisher%20Navoiy.%20Xamsa.%20Hayratul-abror%20(nazm).pdf')


@dp.callback_query_handler(text='f1')
async def n(call: CallbackQuery):
    await call.message.answer('https://e-library.namdu.uz/84%20Badiy%20adabyot%20asarlar/%D0%A2%D0%B0%D1%85%D0%B8%D1%80%20%D0%9C%D0%B0%D0%BB%D0%B8%D0%BA.%20%D0%A2%D0%B0%D0%BB%D0%B2%D0%B0%D1%81%D0%B0.%20%D0%9E%D0%B7%D0%BE%D0%B4%20%D0%98%D0%BD%D1%81%D0%BE%D0%BD%20%D1%85%D0%B0%D0%BA%D0%B8%D0%B4%D0%B0%20%D0%BA%D1%83%D1%88%D0%B8%D0%BA.pdf')


@dp.callback_query_handler(text='f2')
async def n(call: CallbackQuery):
    await call.message.answer('https://library.samdu.uz/files/f229f7ed2e8f42677ceb9ddb16a80b18_Dunyoning%20ishlari.pdf')


@dp.callback_query_handler(text='f3')
async def n(call: CallbackQuery):
    await call.message.answer('https://library.samdukf.uz/files/dd4bec589cbabe4ac3d89cd7035872bd_Bahor%20qaytmaydi.pdf')



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
