import math

from aiogram import executor
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, ContentType, ChatType
from config import dp
from knopkalar.inline import nout_btn, buy_btn
from knopkalar.reply import start_btn
from statelar.my_state import PersonalData


@dp.message_handler(CommandStart(), state=None)
async def start(msg: Message):
    img = open('rasmlar/photo_2023-05-26_16-56-24.jpg', 'rb')
    text = f'Salom {msg.from_user.full_name}👋\n🏪Botimizga hush kelibsiz...\nKerakli bo\'limni tanlang'
    await msg.answer_photo(img, caption=text, reply_markup=start_btn)


@dp.message_handler(text='💻Noutbuklar')
async def noutbuk(msg: Message):
    img = open('rasmlar/2.jpeg', 'rb')
    text = '1.Asus\n2.Acer\n3.Lenovo\n4.Macbook'
    await msg.answer_photo(img, caption=text, reply_markup=nout_btn)


@dp.callback_query_handler(text='1')
async def bir(call: CallbackQuery):
    rasm = open('rasmlar/3.jpeg', 'rb')
    text = 'Xarakteristika:\n😇Core i9\n😅Operativka: 32 GB\n🙃Doimiy xortira: 4 Tb'
    await call.message.answer_photo(rasm, caption=text, reply_markup=buy_btn)


@dp.callback_query_handler(text='buy')
async def buy(call: CallbackQuery):
    await call.message.answer('To\'liq ism-familiyangizni kiriting...')
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def names(msg: Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {
            'name': name
        }
    )
    await msg.answer('Emailni kiriting...')
    # await PersonalData.email.set()
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
    email = data.get('email')
    phone = data.get('phone')

    msgs = 'Quyidagi ma\'lumotlar qabul qilindi:\n'
    msgs += f'Ims: {name}\n'
    msgs += f'Email: {email}\n'
    msgs += f'Phone: {phone}\n'

    await msg.answer(msgs)
    await state.finish()
    # await state.reset_state()


@dp.message_handler(content_types=ContentType.CONTACT)
async def contact(msg: Message):
    await msg.answer('Kontakt qabul qilindi')


@dp.message_handler(content_types=ContentType.LOCATION)
async def contact(msg: Message):
    await msg.answer('Manzilingiz qabul qilindi')


@dp.message_handler(content_types=ContentType.VOICE)
async def contact(msg: Message):
    await msg.answer('Darsdaman eshitolmayman')


@dp.message_handler(content_types=ContentType.STICKER)
async def contact(msg: Message):
    await msg.answer('🤣')


@dp.message_handler(content_types='photo')
async def contact(msg: Message):
    await msg.answer('qanaqa rasm bu?')


@dp.message_handler(content_types=ContentType.AUDIO)
async def contact(msg: Message):
    await msg.answer('Bunaqa nasheda tashlama qamalib ketasan')


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_example(msg: Message):
    await msg.answer('Yeee, akang kuchaydi!')


FORBIDDEN_PHRASE = [
    'ahmoq',
    'telba',
]


@dp.message_handler(text_contains='ahmoq')
async def text_example(msg: Message):
    await msg.reply("So'kish mumkin emas!")


@dp.message_handler(filters.Text(equals='assalom alaykum', ignore_case=True))
async def text_example(msg: Message):
    await msg.reply('Vaalaykum assalom')


@dp.message_handler(filters.Text(contains='assalom', ignore_case=True))
async def text_example(msg: Message):
    await msg.reply('vaalaykum assalom1')




# IsReplyFilter
@dp.message_handler(is_reply=True)
async def reply_filter_example(msg: Message):
    await msg.answer(msg.reply_to_message.from_user.id)

# IsSenderContact
@dp.message_handler(content_types='contact', is_sender_contact=True)
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def sender_contact_example(msg: Message):
    await msg.answer('Rahmat, kontaktingiz qabul qilindi!')

# ForwardedMessageFilter
@dp.message_handler(is_forwarded=True)
async def forwarded_example(msg: Message):
    await msg.answer('Birovning xabarini menga yuborayapsizmi?')

# ChatTypeFilter
# @dp.message_handler(chat_type='private', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(ChatType.PRIVATE), commands='shaxsiy')
async def chat_type_example(msg: Message):
    await msg.answer('Bu shaxsiy chat')




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
