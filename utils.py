# -*- coding: utf-8 -*-
from telebot import types


def generate_markup(answers):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    list_items = []
    for item in answers:
        list_items.append(item)
    for item in list_items:
        markup.add(item)
    return markup


def e646():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_items = []
    list_items.append("Войти в 646")
    for item in list_items:
        markup.add(item)
    return markup


def actions(answer):
    replys = {"Да":"Выкладывай", "Пойдем курить":"Всегда за", "Куда положить печенье?":"*Triggered*",
              "Как принимать матпомощь?":"..."}
    try:
        reply = replys[answer]
    except KeyError as e:
        reply = "Говори четче, что ты там мямлишь"
    return reply