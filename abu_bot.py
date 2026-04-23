import telebot
from telebot import types

TOKEN = "8648041673:AAHWpP3LJt85MlkLBs9-vzGflKeZNmnEN8k"
ADMIN_ID = 8443902786

bot = telebot.TeleBot(TOKEN)
orders = {}

def menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📹 Xizmatlar", "💰 Narxlar")
    kb.row("🛒 Buyurtma berish", "📞 Aloqa")
    kb.row("ℹ️ Biz haqimizda")
    return kb

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Assalomu alaykum!\n\n"
        "Abu Security Solutions botiga xush kelibsiz.\n"
        "Uyingiz va biznesingiz doimo nazoratingizda!\n\n"
        "Kerakli bo‘limni tanlang."
    )
    bot.send_message(message.chat.id, text, reply_markup=menu())

@bot.message_handler(func=lambda message: message.text == "📹 Xizmatlar")
def services(message):
    text = (
        "📹 Xizmatlarimiz:\n\n"
        "✅ IP kameralar\n"
        "✅ Wi‑Fi kameralar\n"
        "✅ 4G kameralar\n"
        "✅ Batareyali kameralar\n"
        "✅ Telefon orqali nazorat\n"
        "✅ Professional montaj\n"
        "✅ Kafolatli xizmat"
    )
    bot.send_message(message.chat.id, text, reply_markup=menu())

@bot.message_handler(func=lambda message: message.text == "💰 Narxlar")
def prices(message):
    text = (
        "💰 Taxminiy narxlar:\n\n"
        "📷 Wi‑Fi kamera: 300 000 so‘mdan\n"
        "📷 IP kamera: 450 000 so‘mdan\n"
        "📷 4G kamera: 650 000 so‘mdan\n"
        "📷 Batareyali kamera: 800 000 so‘mdan\n\n"
        "Aniq narx obyekt va montajga qarab belgilanadi."
    )
    bot.send_message(message.chat.id, text, reply_markup=menu())

@bot.message_handler(func=lambda message: message.text == "📞 Aloqa")
def contact(message):
    text = (
        "📞 Aloqa:\n\n"
        "Telefon: +998 20 015 41 41\n"
        "Telegram: @ASS_adm1n\n"
        "Instagram: @ass__uz\n"
        "Sayt: ASS.uz"
    )
    bot.send_message(message.chat.id, text, reply_markup=menu())

@bot.message_handler(func=lambda message: message.text == "ℹ️ Biz haqimizda")
def about(message):
    text = (
        "ℹ️ Biz haqimizda:\n\n"
        "Abu Security Solutions\n"
        "✅ Uzoq yillik tajriba\n"
        "✅ Sifatli montaj\n"
        "✅ 24 soat ichida xizmat\n"
        "✅ Uy, ofis, do‘kon va tashqi hududlar uchun kameralar"
    )
    bot.send_message(message.chat.id, text, reply_markup=menu())

@bot.message_handler(func=lambda message: message.text == "🛒 Buyurtma berish")
def order_start(message):
    orders[message.chat.id] = {}
    msg = bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    orders[message.chat.id]["name"] = message.text
    msg = bot.send_message(message.chat.id, "Telefon raqamingizni kiriting:")
    bot.register_next_step_handler(msg, get_phone)

def get_phone(message):
    orders[message.chat.id]["phone"] = message.text
    msg = bot.send_message(message.chat.id, "Manzilingizni kiriting:")
    bot.register_next_step_handler(msg, get_address)

def get_address(message):
    orders[message.chat.id]["address"] = message.text
    msg = bot.send_message(message.chat.id, "Nechta va qanday kamera kerak?")
    bot.register_next_step_handler(msg, get_camera)

def get_camera(message):
    orders[message.chat.id]["camera"] = message.text
    data = orders[message.chat.id]

    bot.send_message(
        message.chat.id,
        "✅ Buyurtmangiz qabul qilindi. Tez orada siz bilan bog‘lanamiz.",
        reply_markup=menu()
    )

    admin_text = (
        "🛒 Yangi buyurtma!\n\n"
        f"👤 Ism: {data['name']}\n"
        f"📞 Telefon: {data['phone']}\n"
        f"📍 Manzil: {data['address']}\n"
        f"📹 Buyurtma: {data['camera']}\n"
        f"🆔 User ID: {message.chat.id}"
    )
    bot.send_message(ADMIN_ID, admin_text)

@bot.message_handler(func=lambda message: True)
def other(message):
    bot.send_message(message.chat.id, "Iltimos, menyudan tanlang yoki /start bosing.", reply_markup=menu())

print("Bot ishga tushdi...")
bot.infinity_polling()