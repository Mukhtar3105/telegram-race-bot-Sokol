from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Вставь сюда свой токен
BOT_TOKEN = "7986450530:AAEHTmcGHEyHdCvjU7HRYcqRf17hsQCgoN8"

# Приветственное сообщение
WELCOME_MESSAGE = '🏁 Добро пожаловать! Вы будете получать уведомления о дрэг-заездах.'

# Клавиатура меню
keyboard = [
    ["🔍 Регистрация", "💨 Результаты"],
    ["📊 Классы", "🔥 ТОП 10"],
    ["💬 Чат", "🏁 Online"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Команда /start или /menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=markup)

# Все остальные текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=markup)

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Бот запущен и работает.")
    app.run_polling()
