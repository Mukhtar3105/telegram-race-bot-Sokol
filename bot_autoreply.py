from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 ВСТАВЬ СВОЙ ТОКЕН
BOT_TOKEN = '7986450530:AAEHTmcGHEyHdCvjU7HRYcqRf17hsQCgoN8'

WELCOME_MESSAGE = '🏁 Добро пожаловать! Вы будете получать уведомления о дрэг-заездах.'

# Меню-клавиатура
keyboard = [
    ["🔍 Регистрация", "💨 Результаты"],
    ["📊 Классы", "🔥 ТОП 10"],
    ["💬 Чат", "🏁 Online"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=markup)


# Команда /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выберите действие из меню 👇", reply_markup=markup)


# Ответ на любые другие сообщения
async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=markup)


# Точка входа
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))

    print("✅ Бот запущен...")
    app.run_polling()
