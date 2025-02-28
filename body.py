import time
from telebot import types
from functions import *
from settings import *

def setup_bot(bot):
    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        send_startup_message(bot, message)
        time.sleep(2)  # Пауза перед отправкой приветственного текста
        send_welcome_text(bot, message)
        time.sleep(2)  # Пауза перед отправкой фото профиля
        send_profile_photo(bot, message)
        time.sleep(2)  # Пауза перед отправкой приветственного видео
        send_welcome_video(bot, message)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("start_lesson_"))
    def start_lesson(call):
        lesson_number = int(call.data.split("_")[-1])
        time.sleep(2)  # Пауза перед началом урока
        send_lesson_video(bot, call, lesson_number)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("start_task_"))
    def start_task(call):
        lesson_number = int(call.data.split("_")[-1])
        time.sleep(2)  # Пауза перед началом задания
        initialize_user_questions(call.message.chat.id, lesson_number)
        ask_first_question(bot, call.message.chat.id)

    @bot.message_handler(func=lambda message: message.chat.id in user_question_state)
    def handle_answers(message):
        process_answer(bot, message)

    @bot.message_handler(commands=["help"])
    def send_help(message):
        bot.send_message(message.chat.id, "Используйте команды: /start, /help.")

