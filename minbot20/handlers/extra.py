from aiogram import types, Dispatcher
from bot_instance import bot
#Кости
#Удаляет матерные слова
async def echo_and_ban(message: types.Message):
    ban_words = ['bitch', 'slut', 'java', 'python is bad']
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Вы забанены за плохие слова!!!")
    #Игра в кости
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji='🎲')

    # if message.text.lower()in ban_words:
    #     await message.reply('Это слово плохое Бот админ его удалил!!!')
    #     await bot.delete_message(message.chat.id, message.message_id)




#echo bot
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(message.text)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban, content_types=['text'])