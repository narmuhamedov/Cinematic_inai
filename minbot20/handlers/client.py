from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from bot_instance import dp, bot


#приветствие бота по нашему никнейму
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello my master: {message.from_user.full_name}')


#делаем викторину
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

#викторина с фотками
#1
async def task_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая задача",
                                         callback_data='next_task1')
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

#Регистрируем наши функции
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(task_1, commands=['tasks'])