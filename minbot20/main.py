from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from decouple import config



TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

#приветствие бота по нашему никнейму
@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello my master: {message.from_user.full_name}')


#викторина с фотками
#1
@dp.message_handler(commands=['tasks'])
async def task_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая задача",
                                         callback_data='next_task')
    markup.add(button_call_1)
    question1 = 'Вывод:'
    answers = ['0.0', '4', '3.3', 'error']
    photo = open('media/Screenshot_4.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question1,
        options=answers,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup


    )
#2
@dp.callback_query_handler(lambda func: func.data=='next_task')
async def games_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая задача', callback_data='next_task3')
    markup.add(button_call_2)
    question = 'Вывод:'
    answers = ['1', '2', '3', 'error']
    photo = open('media/Screenshot_1.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=1,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup


    )

#3
@dp.callback_query_handler(lambda func: func.data=='next_task3')
async def games_1(call: types.CallbackQuery):
    question = 'Что за соц сеть:'
    answers = ['Google Meet', 'Zoom', 'Telegram', 'error']
    photo = open('media/Screenshot_3.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',


    )








#делаем викторину
@dp.message_handler(commands='quiz')
async def quiz_1(message: types.Message):
    question = "Зимой и летом одним цветом?"
    answer = ['елка', 'дом', 'человек']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=10,
                        explanation='Как ты мог не отгадать детскую загадку?',
                        explanation_parse_mode=ParseMode.MARKDOWN_V2
                        )









#echo bot
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)



if __name__== "__main__":
    executor.start_polling(dp, skip_updates=False)