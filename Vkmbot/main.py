from aiogram import executor
from aiogram.types import ReplyKeyboardRemove, Message, CallbackQuery, InputFile
from config import dp, bot
from knopkalar.inline_knopka import start_btn, menu_btn1, menu_btn2, menu_btn3


@dp.message_handler(commands='start')
async def start(message: Message):
    photo = open('rasmlar/vkm.png', 'rb')
    matn = f'Salom {message.from_user.first_name}👋, Botimizga hush kelibsiz!'
    a = "Musiqalarni korish uchun knopkani bosing"
    await message.answer_photo(photo, caption=matn)
    await message.answer(a, reply_markup=start_btn)


@dp.message_handler(commands='help')
async def start(message: Message):
    photo = open('rasmlar/help.jpeg', 'rb')
    matn = f'Salom{message.from_user.first_name}👋\nYordam uchun +998(95) 355-39-88 ga murojaat qiling.'
    await message.answer_photo(photo, caption=matn)


@dp.callback_query_handler(text='click')
async def click(call: CallbackQuery):
    text = '1.Ghea Indrawari - Jiwa Yang Bersedih\n2.Jaloliddin Ahmadaliyev - Ketavering yalinmayman\n3.Jaloliddin Ahmadaliyev - O_zim (alam alam) (daydi)\n4.JALOLIDDIN_AHMADALIYEV_MENDA_QOLMADI_DIL_YOR_BIZDAN_KETDI_2_YAGZON'
    await call.message.answer(text, reply_markup=menu_btn1)


@dp.callback_query_handler(text='next1')
async def click(call: CallbackQuery):
    text = '1.Ghea Indrawari - Jiwa Yang Bersedih\n2.Jaloliddin Ahmadaliyev - Ketavering yalinmayman\n3.Jaloliddin Ahmadaliyev - O_zim (alam alam) (daydi)\n4.JALOLIDDIN_AHMADALIYEV_MENDA_QOLMADI_DIL_YOR_BIZDAN_KETDI_2_YAGZON'
    text2 = '1.Jichcha Yomonman (Shox.uz)\n2.Latto, BTS JungKook - Seven\n3.Makeba   Jain\n4.Mirjalol Nematov - Zara [www.Voydoda.Com]'
    text3 = '1.myke_towers_lala_lyric_video_mp3_803\n2.ozoda_nursaidova_alamlar_68\n3.shoxrux-ummon-feat-milena-madmusayeva-soxtalar\n4.yulduz-usmonova-ft-malik-da-kujo-shumo'
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text2, reply_markup=menu_btn2)


@dp.callback_query_handler(text='next2')
async def click(call: CallbackQuery):
    text = '1.Ghea Indrawari - Jiwa Yang Bersedih\n2.Jaloliddin Ahmadaliyev - Ketavering yalinmayman\n3.Jaloliddin Ahmadaliyev - O_zim (alam alam) (daydi)\n4.JALOLIDDIN_AHMADALIYEV_MENDA_QOLMADI_DIL_YOR_BIZDAN_KETDI_2_YAGZON'
    text3 = '1.myke_towers_lala_lyric_video_mp3_803\n2.ozoda_nursaidova_alamlar_68\n3.shoxrux-ummon-feat-milena-madmusayeva-soxtalar\n4.yulduz-usmonova-ft-malik-da-kujo-shumo'
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text3, reply_markup=menu_btn3)


@dp.callback_query_handler(text='back2')
async def click(call: CallbackQuery):
    text = '1.Ghea Indrawari - Jiwa Yang Bersedih\n2.Jaloliddin Ahmadaliyev - Ketavering yalinmayman\n3.Jaloliddin Ahmadaliyev - O_zim (alam alam) (daydi)\n4.JALOLIDDIN_AHMADALIYEV_MENDA_QOLMADI_DIL_YOR_BIZDAN_KETDI_2_YAGZON'
    text3 = '1.1myke_towers_lala_lyric_video_mp3_803\n2.ozoda_nursaidova_alamlar_68\n3.shoxrux-ummon-feat-milena-madmusayeva-soxtalar\n4.yulduz-usmonova-ft-malik-da-kujo-shumo'
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text, reply_markup=menu_btn1)


@dp.callback_query_handler(text='back3')
async def click(call: CallbackQuery):
    text2 = '1.Jichcha Yomonman (Shox.uz)\n2.Latto, BTS JungKook - Seven\n3.Makeba   Jain\n4.Mirjalol Nematov - Zara [www.Voydoda.Com]'
    text3 = '1.myke_towers_lala_lyric_video_mp3_803\n2.ozoda_nursaidova_alamlar_68\n3.shoxrux-ummon-feat-milena-madmusayeva-soxtalar\n4.yulduz-usmonova-ft-malik-da-kujo-shumo'
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text2, reply_markup=menu_btn2)


# @dp.callback_query_handler(text='x')
# async def del(call: CallbackQuery):
#     await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text='1')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Ghea Indrawari - Jiwa Yang Bersedih.mp3'))


@dp.callback_query_handler(text='2')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Jaloliddin Ahmadaliyev - Ketavering yalinmayman.mp3'))


@dp.callback_query_handler(text='3')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Jaloliddin Ahmadaliyev - O_zim (alam alam) (daydi).mp3'))


@dp.callback_query_handler(text='4')
async def click(call: CallbackQuery):
    await call.message.answer_audio(
        InputFile('music/JALOLIDDIN_AHMADALIYEV_MENDA_QOLMADI_DIL_YOR_BIZDAN_KETDI_2_YAGZON.mp3'))


@dp.callback_query_handler(text='5')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Jichcha Yomonman (Shox.uz).mp3'))


@dp.callback_query_handler(text='6')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Latto, BTS JungKook - Seven.mp3'))


@dp.callback_query_handler(text='7')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Makeba   Jain.mp3'))


@dp.callback_query_handler(text='8')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/Mirjalol Nematov - Zara [www.Voydoda.Com].mp3'))


@dp.callback_query_handler(text='9')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/myke_towers_lala_lyric_video_mp3_803.mp3'))


@dp.callback_query_handler(text='10')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/ozoda_nursaidova_alamlar_68.mp3'))


@dp.callback_query_handler(text='11')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/shoxrux-ummon-feat-milena-madmusayeva-soxtalar.mp3'))


@dp.callback_query_handler(text='12')
async def click(call: CallbackQuery):
    await call.message.answer_audio(InputFile('music/yulduz-usmonova-ft-malik-da-kujo-shumo.mp3'))


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
