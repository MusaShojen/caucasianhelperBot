
import telebot
from telebot import types


from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")



bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)



# TARGET_CHAT_ID = '@kavkasusa'  # Замените на идентификатор целевого чата
TARGET_CHAT_ID = None


@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = 'Ас саляму аляйкум уа рахматуЛЛаhи уа баракятух! Я разработан для того, чтобы пересылать ваши сообщения в один из наших чатов анонимно! Это нужно, чтобы не допустить фитну! Чтобы отправить сообщение напиши комнаду /send ! '
    bot.send_message(message.chat.id, welcome_message )

@bot.message_handler(commands=['send'])
def send(message):
    send_message = "Выбери целевой чат с помощью кнопок ниже:"
    markup = types.InlineKeyboardMarkup(row_width=2)

    button1 = types.InlineKeyboardButton('Кавказский Стамбул', callback_data='chat1')
    button2 = types.InlineKeyboardButton('Кавказская Саудия', callback_data='chat2')
    button3 = types.InlineKeyboardButton('Кавказский Дубай', callback_data='chat3')
    button4 = types.InlineKeyboardButton('Кавказская Европа', callback_data='chat4')

    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, send_message, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global TARGET_CHAT_ID

    # Обработка кнопок
    if call.data == 'chat1':
        TARGET_CHAT_ID = '@kafkazist'
    elif call.data == 'chat2':
        TARGET_CHAT_ID = '@kavkazsaudia'
    elif call.data == 'chat3':
        TARGET_CHAT_ID = '@kavkasdubai'
    elif call.data == 'chat4':
        TARGET_CHAT_ID = '@kavkazeurope'

    bot.send_message(call.message.chat.id, f'Целевой чат установлен: {TARGET_CHAT_ID}')
# @bot.message_handler(func=lambda message: True)
#
#
# if message.chat.type == "private"
#     # private chat message
# else:
#     # non-private chat message
#
# bot.polling(non_stop=True)
@bot.message_handler(func=lambda message: True)
def duplicate_and_send(message):
    if message.chat.type == "private":
        # Личное сообщение
        duplicated_text = f"Анонимное сообщение (личное): {message.text}"
        bot.send_message(TARGET_CHAT_ID, duplicated_text)

        # Условие наличия chat.type == "group", "supergroup" или "channel" можно убрать,
        # чтобы дать боту игнорировать все другие типы чатов
    elif message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "channel":
        pass  # Ничего не отправлять для групп, супергрупп и каналов

bot.polling(non_stop=True)


# import logging
#
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
#
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
#
# CHAT_ID = '@kavkasusa'
#
# async def send_hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await context.bot.send_message(chat_id=CHAT_ID, text="Привет, я бот! Как дела?")
#
# async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_message = update.message.text
#     await context.bot.send_message(chat_id=CHAT_ID, text=f'User said: {user_message}')
#     await context.bot.send_message(chat_id=update.effective_chat.id, text='Your message was forwarded to the chat.')
#
# async def command_at_start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот. Как я могу вам помочь?")
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
#
# #
# # if __name__ == '__main__':
# #     application = ApplicationBuilder().token('6276116639:AAEZOB5gP_kj3LzE-4bVltRcAIfFId18w_U').build()
# #
# #     start_handler = CommandHandler('start', start)
# #     application.add_handler(start_handler)
# #     application.add_handler(CommandHandler("sayhello", send_hello))
# #     application.run_polling()
#
# if __name__ == '__main__':
#     application = ApplicationBuilder().token('6276116639:AAEZOB5gP_kj3LzE-4bVltRcAIfFId18w_U').build()
#
# message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message)
# start_handler = CommandHandler("start", command_at_start_callback)
#
# application.add_handler(message_handler)
# application.add_handler(start_handler)
# application.run_polling()
#
#
# # if __name__ == '__main__':
# #     application = ApplicationBuilder().token('YOUR_TOKEN_HERE').build()
# #
# #     start_handler = CommandHandler('start', start)
# #     application.add_handler(start_handler)
# #
# #     message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message)
# #     application.add_handler(message_handler)
# #
# #     application.run_polling()