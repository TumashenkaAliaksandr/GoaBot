import re, os
import telebot
import book, stickers
from string import Template
from telebot import types
import config, btn

# РУССКОЕ МЕНЮ
rMenu = btn.russian_menu
rMenuReg = btn.russian_menuR
# АНГЛИЙСКОЕ МЕНЮ
eMenu = btn.english_menu

bot = telebot.TeleBot(config.TOKEN)

# регистрация пользователя
user_dict = {}


class User:
    def __init__(self, nickname, photo, document):
        self.nickname = nickname
        self.photo = photo
        self.document = document

        keys = book.keyReg

        for key in keys:
            self.key = None


@bot.message_handler(commands=["reg"])
def user_reg(message):
    chat_id = message.chat.id

    if message.text == '/reg':
        bot.send_message(chat_id, 'Напишите свой никнейм: ')
        bot.register_next_step_handler(message, user_reg)
        return

    user_dict[chat_id] = User(message.text, message.photo, message.document)

    bot.send_sticker(message.chat.id, stickers.sticker)
    msg = bot.send_message(chat_id, 'Пришлите фото профиля:')
    bot.register_next_step_handler(msg, process_photo_step)


@bot.message_handler(content_types=["photo", "document"])
def process_photo_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]

    if message.photo:
        user.photo = message.photo[-1]
        user.photo_id = message.photo[-1].file_id
    elif message.document and message.document.mime_type in ['image/jpeg', 'image/png']:
        user.document = message.document
        user.document_id = message.document.file_id

    else:
        msg = bot.reply_to(message, 'Это не фотография, пришлите пожалуйста фото.')
        bot.register_next_step_handler(msg, process_photo_step)

    msg = bot.send_message(message.chat.id, "Введите фамилию и имя")
    bot.register_next_step_handler(msg, process_fullname_step)


def process_fullname_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.fullname = message.text

    msg = bot.send_message(chat_id, '📅  Введите свой день месяц и год рождения! \n например: ДД.ММ.ГГГГ')
    bot.register_next_step_handler(msg, process_age_step)


cli_age = []


def process_age_step(message):
    pattern = re.compile(
        '(?<!\d)(?:0?[1-9]|[12][0-9]|3[01]).(?:0?[1-9]|1[0-2])(?!\d).(?:19[0-9][0-9]|20[01][0-9])(?!\d)', re.IGNORECASE)
    is_valid = pattern.match(message.text)
    if is_valid:
        cli_age.append(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.age = message.text

        msg = bot.send_message(chat_id, '📞  Ваш номер телефона:')
        bot.register_next_step_handler(msg, process_phone_step)
    else:
        msg = bot.reply_to(message, '😖  Вы ввели не правильную дату, попробуйте еще раз!')
        bot.register_next_step_handler(msg, process_age_step)


cli_phone = []

def process_phone_step(message):
    pattern = re.compile('^(\+)?\d+\D*\d{2}\D*\d{3}\D*\d{2}\D*\d{2}$', re.VERBOSE)
    is_valid = pattern.match(message.text.strip())
    if is_valid:
        cli_phone.append(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, '📧  Ваш email:')
        bot.register_next_step_handler(msg, process_email_step)

    else:
        msg = bot.reply_to(message, '😖  Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)


cli_mail = []  # Хранит в себе почту заявителя

def process_email_step(message):
    pattern = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)',
                         re.IGNORECASE)  # Проверяем совпадает ли паттерн
    is_valid = pattern.match(message.text)
    if is_valid:
        cli_mail.append(message.text)  # Записываем полученную почту

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.email = message.text

        bot.send_message(chat_id, '📝 Проверьте все ли правильно!')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да ', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет ', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(chat_id, getRegData(user, '🗿  Ваш ник нейм: '), parse_mode="Markdown")
        if user.document:
            bot.send_document(chat_id, caption='Ваше фото', data=user.document_id, reply_markup=keyboard)
        elif user.photo:
            bot.send_photo(chat_id, caption='Ваше фото', photo=user.photo_id, reply_markup=keyboard)

    else:
        msg = bot.reply_to(message, '😖  Вы ввели что то другое. Пожалуйста введите корректный e-mail.')
        bot.register_next_step_handler(msg, process_email_step)


def getRegData(user, title):
    t = Template(
        book.Templ
    )
    return t.substitute({
        'title': title,
        'nickname': user.nickname,
        'fullname': user.fullname,
        'age': user.age,
        'phone': user.phone,
        'email': user.email

    })


@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"])  # теперь хэндлер принимает только yes и no
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Приятно познакомиться! Заявка принята! ")
        bot.send_sticker(call.message.chat.id, stickers.sticker8)
        bot.send_message(call.message.chat.id, 'Добро пожалловать в ' + call.message.from_user.first_name,
                         reply_markup=rMenuReg)


    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Давайте попробуем еще раз! ")
        bot.send_message(call.message.chat.id, 'Напишите свой ник нейм: ')
        bot.register_next_step_handler(call.message, user_reg)
