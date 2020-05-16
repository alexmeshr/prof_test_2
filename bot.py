# -*- coding: utf-8 -*-
import config
import telebot
import utils
from telebot import types
bot = telebot.TeleBot(config.token)
notentered = True
@bot.message_handler(content_types=["text"])
def repeat_messages(message):
    global notentered
    answers = ["Да", "Пойдем курить", "Куда положить печенье?", "Как принимать матпомощь?", "Развернуться и выйти"]
    if message.text == "Войти в 646":
        notentered = False
        bot.send_message(message.chat.id, "Вадим: У тебя что-то срочное?",
                         reply_markup=utils.generate_markup(answers))
    else:
        if notentered:
            bot.send_message(message.chat.id, "Ваши дейсвия:", reply_markup=utils.e646())
        elif message.text == "Развернуться и выйти":
            notentered = True
            bot.send_message(message.chat.id, "Вы сбежали.", reply_markup=types.ReplyKeyboardRemove())
        else:
            bot.send_message(message.chat.id, utils.actions(message.text))


if __name__ == '__main__':
     print("it's working")
     bot.infinity_polling()
