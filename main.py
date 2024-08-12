import telebot
from PIL import Image
import requests
from io import BytesIO
from functions import *
from settings import * 

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        with open(WELCOME_VIDEO_PATH, 'rb') as welcome_video:
            bot.send_video_note(message.chat.id, welcome_video)
        
        bot.send_message(message.chat.id, f"""Привет, {message.from_user.first_name}! 👋
Ты в правильном месте и в правильное время.

Всего за 4 простых шага ты поймешь, как в легкости и в кайф зарабатывать от 100 тыс. руб/мес на мини-франшизе
Без огромных вложений ❌
Без долгих вебинаров ❌
С простой пошаговой системой ✅

Самое крутое, что никаких сложных обучений и особых навыков на старте тоже не надо. Ты сможешь начать с нуля и уже в первый месяц увидишь результат.

🏆 За прошлый год с командой создали оборот более 310 млн руб. на мини-франшизе. 
Совокупный доход наших партнеров составил более 100 млн руб. 

И ты тоже можешь стать в их числе! ✅ 

Скорее переходи к первому уроку, там я подробно рассказываю, почему мы выбрали данную систему и что она тебе даст. ⬇""")
        
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
        
    try:
        user_id = message.from_user.id
        photos = bot.get_user_profile_photos(user_id)

        if photos.total_count > 0:
            file_id = photos.photos[0][0].file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            file_url = f'https://api.telegram.org/file/bot{API_TOKEN}/{file_path}'

            response = requests.get(file_url)
            user_avatar = Image.open(BytesIO(response.content))

            template = Image.open(CONGRATULATION_PHOTO_PATH)
            user_avatar = user_avatar.resize(AVATAR_SIZE)

            user_avatar = make_circle(user_avatar)

            template.paste(user_avatar, AVATAR_POSITION, user_avatar)

            output = BytesIO()
            template.save(output, format='PNG')
            output.seek(0)

            bot.send_photo(message.chat.id, photo=output)
        else:
            pass
        
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

bot.polling()
