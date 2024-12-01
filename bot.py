import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Твой токен бота
TOKEN = '7894628510:AAEGifnRrQuelGbyuk9wzrR8nLHsdZ6Dev0'

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я твой бот. Чем могу помочь?')

# Функция для команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Я пока могу немного. Напиши команду /start, чтобы начать.')

# Главная функция для запуска бота
def main():
    # Создаем приложение с помощью токена
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота (без await)
    application.run_polling()

# Запуск главной функции
if __name__ == '__main__':
    main()
