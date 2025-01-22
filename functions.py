import time
import requests
from io import BytesIO
from telebot import types
from settings import *
from utils import *

user_question_state = {}

def send_startup_message(bot, message):
    """
    Отправляет сообщение о запуске бота и отсчитывает время до начала работы.
    """
    startup_message = TEMP_STARTUP_MESSAGE
    sent_message = bot.send_message(message.chat.id, startup_message)
    for i in range(3, 0, -1):
        bot.edit_message_text(
            f"{startup_message} {i}...",
            chat_id=message.chat.id,
            message_id=sent_message.message_id,
        )
        time.sleep(1.5)
    bot.delete_message(message.chat.id, sent_message.message_id)

def send_welcome_text(bot, message):
    """
    Отправляет приветственное сообщение пользователю.
    """
    bot.send_message(
        message.chat.id, f"Привет, {message.from_user.first_name}! 👋\n" + WELCOME_MESSAGE
    )

def send_welcome_video(bot, message):
    """
    Отправляет приветственное видео и кнопку для перехода к первому уроку.
    """
    markup = types.InlineKeyboardMarkup()
    lesson_button = types.InlineKeyboardButton(
        text="Перейти к первому уроку", callback_data="start_lesson_1"
    )
    markup.add(lesson_button)
    with open(WELCOME_VIDEO_PATH, "rb") as video:
        bot.send_video_note(message.chat.id, video, reply_markup=markup)

def send_profile_photo(bot, message):
    """
    Отправляет фото профиля пользователя с поздравительным шаблоном.
    """
    user_id = message.from_user.id
    photos = bot.get_user_profile_photos(user_id)
    if photos.total_count > 0:
        file_id = photos.photos[0][0].file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        file_url = f"https://api.telegram.org/file/bot{BOT_API_TOKEN}/{file_path}"

        response = requests.get(file_url)
        user_avatar = Image.open(BytesIO(response.content))
        user_avatar = user_avatar.resize(AVATAR_SIZE, Image.LANCZOS)
        user_avatar = make_circle(user_avatar)
        template = Image.open(CONGRATULATORY_IMAGE_PATH)
        if template.mode != "RGBA":
            template = template.convert("RGBA")
        template.paste(user_avatar, AVATAR_POSITION, mask=user_avatar.split()[3])
        output = BytesIO()
        template.save(output, format="PNG")
        output.seek(0)
        bot.send_photo(message.chat.id, photo=output)

def send_lesson_video(bot, call, lesson_number):
    """
    Отправляет видеоурок и текст перед заданием.
    """
    lesson_message = f"{globals()[f'LESSON_TEXT_{lesson_number}']}\n{globals()[f'LESSON_LINK_{lesson_number}']}"
    bot.send_message(call.message.chat.id, lesson_message)
    time.sleep(10)
    send_task_image(bot, call, lesson_number)

def send_task_image(bot, call, lesson_number):
    """
    Отправляет изображение задания и текст.
    """
    markup = types.InlineKeyboardMarkup()
    if lesson_number < 3:
        start_button = types.InlineKeyboardButton(
            text="Начать выполнение заданий", callback_data=f"start_task_{lesson_number}"
        )
        markup.add(start_button)
    elif lesson_number == 3:
        registration_button = types.InlineKeyboardButton(
            text="Пройти регистрацию", url=FORM_LINK
        )
        markup.add(registration_button)
    with open(globals()[f'TASK_IMAGE_{lesson_number}_PATH'], "rb") as task_image:
        bot.send_photo(call.message.chat.id, task_image, caption=globals()[f'TASK_{lesson_number}_DESCRIPTION'], reply_markup=markup)

def initialize_user_questions(chat_id, lesson_number):
    """
    Инициализирует состояние вопросов для пользователя.
    """
    user_question_state[chat_id] = {"current": 1, "answers": [], "lesson_number": lesson_number}

def ask_first_question(bot, chat_id):
    """
    Задает первый вопрос пользователю.
    """
    lesson_number = user_question_state[chat_id]["lesson_number"]
    bot.send_message(
        chat_id,
        globals()[f'QUESTION_{lesson_number}_1']
    )

def process_answer(bot, message):
    """
    Обрабатывает ответ пользователя на текущий вопрос.
    """
    user_id = message.chat.id
    current_question_data = user_question_state.get(user_id)

    if not current_question_data:
        return

    lesson_number = current_question_data["lesson_number"]
    current_question = current_question_data["current"]

    if current_question == 1:
        current_question_data["answers"].append(
            f"{globals()[f'QUESTION_{lesson_number}_1']} {message.text}"
        )
        bot.send_message(
            user_id,
            globals()[f'QUESTION_{lesson_number}_2']
        )
        current_question_data["current"] = 2

    elif current_question == 2:
        current_question_data["answers"].append(
            f"{globals()[f'QUESTION_{lesson_number}_2']} {message.text}"
        )
        bot.send_message(
            user_id,
            globals()[f'QUESTION_{lesson_number}_3']
        )
        current_question_data["current"] = 3

    elif current_question == 3:
        current_question_data["answers"].append(
            f"{globals()[f'QUESTION_{lesson_number}_3']} {message.text}"
        )

        user_name = message.from_user.username
        if not user_name:
            user_name = message.from_user.first_name

        bot.send_message(
            ADMIN_ID_ALT,
            f"Ответы пользователя @{user_name}:\n" + "\n".join(current_question_data["answers"]),
        )
        bot.send_message(user_id, "Спасибо! Ваши ответы отправлены на проверку!")
        time.sleep(30)  # Пауза в 30 секунд
        send_voice_message(bot, user_id, lesson_number)
        time.sleep(2)  # Пауза после голосового сообщения
        if lesson_number < 3:
            send_next_lesson_presentation(bot, user_id, lesson_number + 1)
        del user_question_state[user_id]

def send_voice_message(bot, user_id, lesson_number):
    """
    Отправляет голосовое сообщение после отправки ответов на проверку.
    """
    if lesson_number == 1:
        voice_path = VOICE_1_PATH
    elif lesson_number == 2:
        voice_path = VOICE_2_PATH
    else:
        return

    with open(voice_path, "rb") as voice:
        bot.send_voice(user_id, voice)

def send_next_lesson_presentation(bot, user_id, lesson_number):
    """
    Отправляет фото и текст, представляющие следующий урок, а также кнопку для перехода к следующему уроку.
    """
    markup = types.InlineKeyboardMarkup()
    lesson_button = types.InlineKeyboardButton(
        text=f"Перейти к {lesson_number} уроку", callback_data=f"start_lesson_{lesson_number}"
    )
    markup.add(lesson_button)
    with open(globals()[f'TASK_{lesson_number}_PRESENTATION_IMAGE_PATH'], "rb") as presentation_image:
        bot.send_photo(user_id, presentation_image, caption=globals()[f'TASK_{lesson_number}_PRESENTATION_DESCRIPTION'], reply_markup=markup)
