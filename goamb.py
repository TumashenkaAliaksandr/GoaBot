import book, regg, stickers
import btn, market
from telebot import types
from cachetools import keys


user_dict = regg.user_dict

# noinspection PyTypeChecker
class User:
    def __init__(self, nickname, photo, document):
        self.nickname = nickname
        self.photo = photo
        self.document = document

        for key in keys:
            self.key = None

bot = regg.bot
#START
@bot.message_handler(commands=['start'])
def start_message(message):
    #if len(hello_count) == 0:  # Проверяем здоровались ли мы ранее
    bot.send_sticker(message.chat.id, stickers.sticker)
    bot.send_message(message.chat.id, message.from_user.first_name + book.hello)
    bot.send_message(message.chat.id, book.lang, reply_markup=keyboard1)

#МЕНЮ ВЫБОРА ЯЗЫКА
keyboard1 = types.ReplyKeyboardMarkup(True)
keyboard1.row(book.eng, book.rus)
keyboard2 = types.ReplyKeyboardMarkup(True)
keyboard2.row(book.engR, book.rusR, book.can_cel)
keyboard3 = types.ReplyKeyboardMarkup(True)
keyboard3.row(book.eng, book.rus, book.can_cel1)

# РУССКОЕ МЕНЮ
rMenu = btn.russian_menu
rMenuReg = btn.russian_menuR
# АНГЛИЙСКОЕ МЕНЮ
eMenu = btn.english_menu

@bot.message_handler(content_types=['text'])
def send_text(message):
    #Выбор языка
    if message.text == '🇬🇧 English':
        bot.send_message(message.chat.id, book.lang_eng, reply_markup=eMenu)
    elif message.text == 'English 🇬🇧':
        bot.send_message(message.chat.id, book.lang_eng, reply_markup=eMenu)
    elif message.text == '🇷🇺 Русский':
        bot.send_message(message.chat.id, book.lang_rus, reply_markup=rMenu)
    elif message.text == 'Русский 🇷🇺':
        bot.send_message(message.chat.id, book.lang_rus, reply_markup=rMenuReg)
    if message.text == book.can_cel:
        bot.send_message(message.chat.id, book.back_menu, reply_markup=rMenuReg)
    elif message.text == book.can_celEng:
        bot.send_message(message.chat.id, book.back_menuEng, reply_markup=eMenu) # поменять потом на меню после рег англ
    if message.text == book.can_cel1:
        bot.send_message(message.chat.id, book.back_menu, reply_markup=rMenu)
    elif message.text == '/menu':
        bot.send_sticker(message.chat.id,  stickers.sticker1)
        bot.send_message(message.chat.id, book.menu, reply_markup=rMenuReg)
    elif message.text == '/market':
        bot.send_sticker(message.chat.id,  stickers.sticker5)
        bot.send_message(message.chat.id, book.market, reply_markup=btn.Smarket)
    elif message.text == '/settings':
        bot.send_sticker(message.chat.id,  stickers.sticker8)
        bot.send_message(message.chat.id, book.settingCh, reply_markup=btn.Stuning)
    elif message.text == '® Регистрация':
        bot.send_sticker(message.chat.id, stickers.sticker11)
        bot.send_message(message.chat.id, book.reg_one, reply_markup=btn.reg_button)


    if message.text == '/reg':
        bot.send_message(message.chat_id, stickers.sticker2)
        bot.send_message(message, 'Напишите свой ник нейм: ')
        bot.send_message(message, btn.reg_button, regg.user_reg)


    #Русское меню
    elif message.text == '🚗 Мой профиль':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        bot.send_message(message.chat.id, regg.getRegData(user, '🗿  Ваш ник нейм: '), parse_mode="Markdown")
        if user.document:
            bot.send_document(chat_id, caption='Ваше фото', data=user.document_id)
        elif user.photo:
            bot.send_photo(chat_id, caption='Ваше фото', photo=user.photo_id)
    elif message.text == '👳 My profile':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn_back = types.KeyboardButton(book.btnbackEng)
        markup.add( btn_back)
        bot.send_message(message.chat.id, book.my_profileEng)
        bot.send_message(message.chat.id, book.profile_regEng, reply_markup=markup)
    elif message.text == '/profile':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        bot.send_message(message.chat.id, regg.getRegData(user, '🗿  Ваш ник нейм: '), parse_mode="Markdown")
        if user.document:
            bot.send_document(chat_id, caption='Ваше фото', data=user.document_id)
        elif user.photo:
            bot.send_photo(chat_id, caption='Ваше фото', photo=user.photo_id)

#Возврат в главное меню
    elif message.text == '↩ Главное меню':
        bot.send_sticker(message.chat.id, stickers.sticker1)
        bot.send_message(message.chat.id, book.msMenu_back, reply_markup=rMenuReg)
    elif message.text == '🔙 Главное меню':
        bot.send_sticker(message.chat.id, stickers.sticker1)
        bot.send_message(message.chat.id, book.msMenu_back, reply_markup=rMenu)
    elif message.text == '🔙 Назад':
        bot.send_sticker(message.chat.id, stickers.sticker)
        bot.send_message(message.chat.id, book.market_back, reply_markup=btn.market_menu_moto)
    elif message.text == '↩ Назад':
        bot.send_sticker(message.chat.id, stickers.sticker)
        bot.send_message(message.chat.id, book.market_back, reply_markup=btn.market_menu_scooter)
    elif message.text == '🔙 Main menu':
        bot.send_message(message.chat.id, book.msMenu_backEng, reply_markup=eMenu)#Добавить меню второго уровня после рега
#Настройки
    elif message.text == '⚙ Настройки':
        bot.send_sticker(message.chat.id, stickers.sticker1)
        bot.send_message(message.chat.id, book.settingCh, reply_markup=btn.tuning)
    elif message.text == '🛠 Настройки':
        bot.send_sticker(message.chat.id, stickers.sticker7)
        bot.send_message(message.chat.id, book.settingCh, reply_markup=btn.Stuning)

    elif message.text == '⚙ Settings':
        bot.send_sticker(message.chat.id, stickers.sticker1)
        bot.send_message(message.chat.id, book.settingChEng, reply_markup=btn.tuningEng)

#market
    elif message.text == '🏬 Маркет':
        bot.send_sticker(message.chat.id, stickers.sticker3)
        bot.send_message(message.chat.id, book.market, reply_markup=btn.Smarket)
    elif message.text == '🏍 Мотоциклы':
        bot.send_sticker(message.chat.id, stickers.sticker7)
        bot.send_message(message.chat.id, book.market, reply_markup=btn.market_menu_moto)
    elif message.text == '💰 Бюджет':
        bot.send_sticker(message.chat.id, stickers.sticker16)
        bot.send_message(message.chat.id, book.sms_budget, reply_markup=btn.moto_budget)
    elif message.text == '🔰 Премиум':
        bot.send_sticker(message.chat.id, stickers.sticker21)
        bot.send_message(message.chat.id, book.sms_premium, reply_markup=btn.moto_premium)
    elif message.text == '*YAMAHA':
        bot.send_sticker(message.chat.id, stickers.sticker15)
        bot.send_message(message.chat.id, book.ymaha, reply_markup=btn.yamaha_btn)
    elif message.text == 'YAMAHA*':
        bot.send_sticker(message.chat.id, stickers.sticker15)
        bot.send_message(message.chat.id, book.ymaha, reply_markup=btn.yamahapre_btn)
    elif message.text == '*SUZUKI':
        bot.send_sticker(message.chat.id, stickers.sticker17)
        bot.send_message(message.chat.id, book.suzuki, reply_markup=btn.suzuki_btn)
    elif message.text == 'SUZUKI*':
        bot.send_sticker(message.chat.id, stickers.sticker17)
        bot.send_message(message.chat.id, book.suzuki, reply_markup=btn.suzukipre_btn)
    elif message.text == '*HONDA':
        bot.send_sticker(message.chat.id, stickers.sticker18)
        bot.send_message(message.chat.id, book.honda, reply_markup=btn.honda_btn)
    elif message.text == 'HONDA*':
        bot.send_sticker(message.chat.id, stickers.sticker18)
        bot.send_message(message.chat.id, book.honda, reply_markup=btn.hondapre_btn)
    elif message.text == '*ROYAL ENFIELD':
        bot.send_sticker(message.chat.id, stickers.sticker19)
        bot.send_message(message.chat.id, book.royal, reply_markup=btn.royal_btn)
    elif message.text == 'ROYAL ENFIELD*':
        bot.send_sticker(message.chat.id, stickers.sticker19)
        bot.send_message(message.chat.id, book.royal, reply_markup=btn.royalpre_btn)
    elif message.text == '*BAJAJ':
        bot.send_sticker(message.chat.id, stickers.sticker20)
        bot.send_message(message.chat.id, book.bajaj, reply_markup=btn.bajaj_btn)
    elif message.text == 'BAJAJ*':
        bot.send_sticker(message.chat.id, stickers.sticker20)
        bot.send_message(message.chat.id, book.bajaj, reply_markup=btn.bajajpre_btn)
    elif message.text == 'BMW*':
        bot.send_sticker(message.chat.id, stickers.sticker22)
        bot.send_message(message.chat.id, book.bajaj, reply_markup=btn.bmwpre_btn)
    elif message.text == 'BENELLI*':
        bot.send_sticker(message.chat.id, stickers.sticker23)
        bot.send_message(message.chat.id, book.bajaj, reply_markup=btn.benellipre_btn)
    elif message.text == '🏍 Все модели':
        bot.send_sticker(message.chat.id, stickers.sticker10)
        bot.send_message(message.chat.id, book.market_mot, reply_markup=btn.rent_menu_moto)

    elif message.text == '🛵 Скутера':
        bot.send_sticker(message.chat.id, stickers.sticker7)
        bot.send_message(message.chat.id, book.market, reply_markup=btn.market_menu_scooter)
    elif message.text == '🛵 Все модели':
        bot.send_sticker(message.chat.id, stickers.sticker13)
        bot.send_message(message.chat.id, book.market_sk, reply_markup=btn.rent_menu_scooter)

#favorites '⭐ Избранное'
    elif message.text == '⭐ Избранное':
        bot.send_sticker(message.chat.id, stickers.sticker21)
        bot.send_message(message.chat.id, book.fav_tes, reply_markup=btn.market_menu_favorites)

#information
    elif message.text == '📰 Информация':
        bot.send_sticker(message.chat.id, stickers.sticker12)


@bot.callback_query_handler(func=lambda call: call.data in ["lang", "lang1", "faq", "faq1", "langEng", "faqEng"])  # теперь хэндлер принимает только
def callback_worker(call):
    if call.data == "lang":
        bot.send_message(call.message.chat.id, '👅 Выберите язык',
                         reply_markup=keyboard2)
    elif call.data == "langEng":
        bot.send_message(call.message.chat.id, '👅 Change language ',
                         reply_markup=keyboard3)
    elif call.data == "lang1":
        bot.send_message(call.message.chat.id, '👅 Выберите язык',
                         reply_markup=keyboard3)
    elif call.data == "faq":
        bot.send_message(call.message.chat.id, book.faq)
    elif call.data == "faq1":
        bot.send_message(call.message.chat.id, book.faq)
    elif call.data == "faqEng":
        bot.send_message(call.message.chat.id, book.faqEng)


# RUN
bot.polling(none_stop=True)