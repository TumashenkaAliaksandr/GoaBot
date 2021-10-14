from telebot import types


#русское меню
russian_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
russian_menu.row('🏍 Мотоциклы', '🛵 Скутера', '🚗 Машины')
russian_menu.row('⭐ Избранное', '⚙ Настройки')
russian_menu.row('® Регистрация', '📰 Информация')


russian_menuR = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
russian_menuR.row('🚗 Мой профиль', '🏬 Маркет', '🍖 Еда', '🏡 Аренда жилья')
russian_menuR.row('⭐ Избранное', '📰 Новости', '➕ Кинуть ссыл', '🛠 Настройки')

# Английское меню
english_menu = types.ReplyKeyboardMarkup(True)
english_menu.row('👤 /reg', '🛒 Market', '📰 News', '⚙ Settings')

# кнопка рег/ назад в главное меню(rus/eng)
reg_button = types.ReplyKeyboardMarkup(True)
reg_button.row('/reg')
reg_button.row('🔙 Главное меню')

back = types.ReplyKeyboardMarkup(True)
back.row('🔙 Главное меню')
backEng = types.ReplyKeyboardMarkup(True)
backEng.row('🔙 Main menu')


# маркет
Smarket = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Smarket.row('📰 Подать объявление')
Smarket.row('🏍 Мотоциклы', '🛵 Скутера', '🚗 Машины', '🌌 Прочее')
Smarket.row('↩ Главное меню')

#МЕНЮ кнопки Настройки ЯЗЫК ru/eng
tuning = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='👄 Изменить язык', callback_data='lang1')
item2 = types.InlineKeyboardButton(text='🗣⁉️ Частые вопросы', callback_data='faq1')
tuning.add(item1, item2)

Stuning = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='👅 язык', callback_data='lang')
item2 = types.InlineKeyboardButton(text='🗣 Никнейм', callback_data='nickname')
item3 = types.InlineKeyboardButton(text='📪 email', callback_data='email')
item4 = types.InlineKeyboardButton(text='📱 Телефон', callback_data='phone')
item5 = types.InlineKeyboardButton(text='⁉️ Частые вопросы', callback_data='faq')
Stuning.add(item1, item2, item3, item4, item5)

tuningEng = types.InlineKeyboardMarkup()
itemEng1 = types.InlineKeyboardButton(text='👄 Change language', callback_data='langEng')
itemEng2 = types.InlineKeyboardButton(text='🗣⁉️ FAQ', callback_data='faqEng')
tuningEng.add(itemEng1, itemEng2)

#market
Smarket_menu_moto = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3 )
Smarket_menu_moto.row('🏍 Все модели')
Smarket_menu_moto.row('👴 Старые', '🔰 Новые', '💰 Бюджет')
Smarket_menu_moto.row('↩ Главное меню')

market_menu_moto = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
market_menu_moto.row('💰 Бюджет', '🔰 Премиум', '👴 Эксклюзив')
market_menu_moto.row('🏍 Все модели')
market_menu_moto.row('🔙 Главное меню')

market_menu_scooter = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
market_menu_scooter.row('Бюджет 💰', 'Премиум 🔰', 'Эксклюзив 👴')
market_menu_scooter.row('🛵 Все модели')
market_menu_scooter.row('🔙 Главное меню')

# прокат
rent_menu_moto = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
rent_menu_moto.row('YAMAHA', 'BAJAJ', 'ROYAL ENFIELD')
rent_menu_moto.row('HONDA', 'BMW', 'BENELLI')
rent_menu_moto.row('🔙 Назад')

rent_menu_scooter = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
rent_menu_scooter.row('YAMAHA', 'VESPA', 'HONDA')
rent_menu_scooter.row('↩ Назад')

# купить
buy_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
buy_menu.row('BAJAJ', 'BMW', 'BENELLI')
buy_menu.row('YAMAHA', 'SUZUKI', 'ROYAL ENFIELD')
buy_menu.row('🔙 Назад')

#мото бюджет
moto_budget = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
moto_budget.row('*YAMAHA', '*SUZUKI', '*HONDA')
moto_budget.row('*ROYAL ENFIELD', '*BAJAJ')
moto_budget.row('🔙 Назад')

#YAMAHA
yamaha_btn = types.InlineKeyboardMarkup(row_width=1)
yam1 = types.InlineKeyboardButton(text='FZ 150', callback_data='faq1')
yam2 = types.InlineKeyboardButton(text='FZ 250', callback_data='faq1')
yam3 = types.InlineKeyboardButton(text='FZ fizer', callback_data='faq1')
yam4 = types.InlineKeyboardButton(text='R15', callback_data='faq1')
yamaha_btn.add(yam1, yam2, yam3, yam4)

#SUZUKI
suzuki_btn = types.InlineKeyboardMarkup(row_width=1)
suz1 = types.InlineKeyboardButton(text='GSX-R150', callback_data='faq1')
suzuki_btn.add(suz1)

#HONDA
honda_btn = types.InlineKeyboardMarkup(row_width=1)
hon1 = types.InlineKeyboardButton(text='Honda - Hero', callback_data='faq1')
honda_btn.add(hon1)

#ROYALENFIELD
royal_btn = types.InlineKeyboardMarkup(row_width=1)
roy1 = types.InlineKeyboardButton(text='Classic 350', callback_data='faq1')
roy2 = types.InlineKeyboardButton(text='Thunderbird 350', callback_data='faq1')
roy3 = types.InlineKeyboardButton(text='Thunderbird  500', callback_data='faq1')
roy4 = types.InlineKeyboardButton(text='Himalayan', callback_data='faq1')
royal_btn.add(roy1, roy2, roy3, roy4)

#BAJAJ
bajaj_btn = types.InlineKeyboardMarkup(row_width=1)
baj1 = types.InlineKeyboardButton(text='Avenger-street-150', callback_data='faq1')
baj2 = types.InlineKeyboardButton(text='Pulsar-220f old', callback_data='faq1')
baj3 = types.InlineKeyboardButton(text='KTM 200 old new', callback_data='faq1')
bajaj_btn.add(baj1, baj2, baj3)

#мото премиум
moto_premium = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
moto_premium.row('YAMAHA*', 'SUZUKI*', 'HONDA*')
moto_premium.row('ROYAL ENFIELD*', 'BAJAJ*')
moto_premium.row('BMW*', 'BENELLI*')
moto_premium.row('🔙 Назад')

#YAMAHApre
yamahapre_btn = types.InlineKeyboardMarkup(row_width=1)
ya1 = types.InlineKeyboardButton(text='FZ 150', callback_data='faq1')
ya2 = types.InlineKeyboardButton(text='FZ 250', callback_data='faq1')
ya3 = types.InlineKeyboardButton(text='FZ fizer', callback_data='faq1')
ya4 = types.InlineKeyboardButton(text='R15', callback_data='faq1')
ya5 = types.InlineKeyboardButton(text='MT150', callback_data='faq1')
yamahapre_btn.add(ya1, ya2, ya3, ya4, ya5)

#SUZUKIpre
suzukipre_btn = types.InlineKeyboardMarkup(row_width=1)
su1 = types.InlineKeyboardButton(text='GSX-R150', callback_data='faq1')
suzukipre_btn.add(su1)

#HONDApre
hondapre_btn = types.InlineKeyboardMarkup(row_width=1)
ho1 = types.InlineKeyboardButton(text='Hero NEW', callback_data='faq1')
ho2 = types.InlineKeyboardButton(text='Hornet 250', callback_data='faq1')
ho3 = types.InlineKeyboardButton(text='Hornet 2.0', callback_data='faq1')
ho4 = types.InlineKeyboardButton(text='Xpulse 200', callback_data='faq1')
ho5 = types.InlineKeyboardButton(text='CBR 250', callback_data='faq1')
hondapre_btn.add(ho1, ho2, ho3, ho4, ho5)

#ROYALENFIELDpre
royalpre_btn = types.InlineKeyboardMarkup(row_width=1)
ro1 = types.InlineKeyboardButton(text='Classic 350', callback_data='faq1')
ro2 = types.InlineKeyboardButton(text='Thunderbird 350', callback_data='faq1')
ro3 = types.InlineKeyboardButton(text='Thunderbird  500', callback_data='faq1')
ro4 = types.InlineKeyboardButton(text='Bullet', callback_data='faq1')
ro5 = types.InlineKeyboardButton(text='Himalayan', callback_data='faq1')
ro6 = types.InlineKeyboardButton(text='GT 535 / 650', callback_data='faq1')
ro7 = types.InlineKeyboardButton(text='Interceptor 650', callback_data='faq1')
ro8 = types.InlineKeyboardButton(text='Meteor 350', callback_data='faq1')
royalpre_btn.add(ro1, ro2, ro3, ro4, ro5, ro6, ro7, ro8)

#BAJAJpre
bajajpre_btn = types.InlineKeyboardMarkup(row_width=1)
baja1 = types.InlineKeyboardButton(text='Avenger-street-150', callback_data='faq1')
baja2 = types.InlineKeyboardButton(text='Avenger-cruise-220', callback_data='faq1')
baja3 = types.InlineKeyboardButton(text='Pulsar-ns200', callback_data='faq1')
baja4 = types.InlineKeyboardButton(text='Pulsar-150', callback_data='faq1')
baja5 = types.InlineKeyboardButton(text='Pulsar-ns125', callback_data='faq1')
baja6 = types.InlineKeyboardButton(text='Pulsar-220f', callback_data='faq1')
baja7 = types.InlineKeyboardButton(text='KTM 125', callback_data='faq1')
baja8 = types.InlineKeyboardButton(text='KTM 200', callback_data='faq1')
baja9 = types.InlineKeyboardButton(text='KTM 250', callback_data='faq1')
baja10 = types.InlineKeyboardButton(text='KTM Duke 390', callback_data='faq1')
bajajpre_btn.add(baja1, baja2, baja3, baja4, baja5, baja6, baja7, baja8, baja9, baja10 )

#BMWpre
bmwpre_btn = types.InlineKeyboardMarkup(row_width=1)
bm1 = types.InlineKeyboardButton(text='BMW 310', callback_data='faq1')
bmwpre_btn.add(bm1)

#BENELLIpre
benellipre_btn = types.InlineKeyboardMarkup(row_width=1)
bene1 = types.InlineKeyboardButton(text='Benelli 600 / 300', callback_data='faq1')
benellipre_btn.add(bene1)

#favorites '⭐ Избранное'
market_menu_favorites = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
market_menu_favorites.row('🔙 Главное меню')