import time
import requests
from telebot import TeleBot
from body import setup_bot
from settings import BOT_API_TOKEN
import signal
import sys

bot = TeleBot(BOT_API_TOKEN)
setup_bot(bot)


def shutdown_signal_handler(signal_num, frame):
    """Обработчик сигнала завершения работы."""
    print("\nПолучен сигнал завершения. Завершаем работу бота...")
    bot.stop_polling()
    print("Бот завершил работу. Программа завершена.")
    sys.exit(0)


signal.signal(signal.SIGINT, shutdown_signal_handler)  
signal.signal(signal.SIGTERM, shutdown_signal_handler)  

if __name__ == "__main__":
    while True:
        try:
            print("Бот запущен!")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            time.sleep(15)
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)
        finally:
            print("Бот завершил работу.")
