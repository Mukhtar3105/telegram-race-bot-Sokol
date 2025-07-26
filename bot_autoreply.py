from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ваш токен
BOT_TOKEN = '7986450530:AAEHTmcGHEyHdCvjU7HRYcqRf17hsQCgoN8'

# Приветственное сообщение
WELCOME_MESSAGE = '🏁 Добро пожаловать! Вы будете получать уведомления о дрэг-заездах.'

# Кнопочное меню
keyboard = [
    ["🔍 Регистрация", "💨 Результаты"],
    ["📊 Классы", "🔥 ТОП 10"],
    ["💬 Чат", "🏁 Online"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)

# Команда /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выберите действие из меню 👇", reply_markup=reply_markup)

# Запуск бота
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))

    print("✅ Бот запущен и слушает команды...")
    app.run_polling()

if __name__ == '__main__':
    main()
