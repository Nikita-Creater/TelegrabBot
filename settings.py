import os

# Путь к корневому каталогу проекта
BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# ID администратора
ADMIN_ID_MAIN = 338211917  # ID основного администратора
ADMIN_ID_MAIN_2 = 325383279
ADMIN_ID_ALT = 1368990782  # ID дополнительного администратора (если потребуется)

# Параметры для аватара
AVATAR_SIZE = (200, 200)
AVATAR_POSITION = (240, 355)

# Токен API для доступа к боту
BOT_API_TOKEN = '7041570903:AAHE5z5mjnYT-iBIxiKjZ4LL3xN2pqCn-c4'

# Пути к медиафайлам
WELCOME_VIDEO_PATH = os.path.join(BASE_DIRECTORY, 'video', 'welcome.mp4')
CONGRATULATORY_IMAGE_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'congratulation1.jpg')
TASK_IMAGE_1_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Tasks', 'task_1.jpeg')
TASK_IMAGE_2_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Tasks', 'task_2.jpeg')
TASK_IMAGE_3_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Tasks', 'task_3.jpeg')
TASK_2_PRESENTATION_IMAGE_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Tasks', 'task_2_presentation.jpg')
TASK_3_PRESENTATION_IMAGE_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Tasks', 'task_3_presentation.jpg')
ACHIEVEMENT_1_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Achievements', '1.jpg')
ACHIEVEMENT_2_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Achievements', '2.jpg')
ACHIEVEMENT_3_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Achievements', '3.jpg')
ACHIEVEMENT_4_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Achievements', '4.jpg')
ACHIEVEMENT_5_PATH = os.path.join(BASE_DIRECTORY, 'photo', 'Achievements', '5.jpeg')

VOICE_1_PATH = os.path.join(BASE_DIRECTORY, 'voices', 'task_1.ogg')
VOICE_2_PATH = os.path.join(BASE_DIRECTORY, 'voices', 'task_2.ogg')

# Тексты сообщений
LESSON_LINK_1 = "https://vk.com/video220558864_456239440"
LESSON_LINK_2 = "https://vk.com/video220558864_456239441?list=ln-z00OZ3xQJ5y7r5O82Z"
LESSON_LINK_3 = "https://vk.com/video220558864_456239442?list=ln-bnhaxw2XlkZHRGLZsA"

LESSON_TEXT_1 = """Смотри первый урок и выполни простое задание👇

Желаем успешно пройти практикум до конца и воплотить свои мечты в жизнь!🤗"""

LESSON_TEXT_2 = """Смотри второй урок и выполни простое задание👇"""

LESSON_TEXT_3 = """Смотри третий урок и выполни простое задание👇"""

WELCOME_MESSAGE = """Ты в правильном месте и в правильное время.

Всего за 3 простых шага ты поймешь, как в легкости и в кайф зарабатывать от 100 тыс. руб/мес на мини-франшизе.
Без огромных вложений ❌
Без долгих вебинаров ❌
С простой пошаговой системой ✅

Самое крутое, что никаких сложных обучений и особых навыков на старте тоже не надо. Ты сможешь начать с нуля и уже в первый месяц увидеть результат.

🏆 За прошлый год мы с командой создали оборот более 310 млн руб. на мини-франшизе.
Совокупный доход наших партнеров составил более 100 млн руб.

И ты тоже можешь стать в их числе! ✅

Скорее переходи к первому уроку, там я подробно расскажу, почему мы выбрали данную систему и что она тебе даст. ⬇"""

TEMP_STARTUP_MESSAGE = """Запуск данного бота - лучшее решение твоего дня!

Бот запустится через """
TASK_1_DESCRIPTION = """Поздравляю тебя с просмотром первого урока🥳

Главная задача на этом этапе - дать тебе уверенность, что у тебя получится зарабатывать удаленно. Чтобы ты перестал переживать за завтрашний день и построил стабильный, прибыльный бизнес.
На уроке ты увидел, как много людей уже используют мини-франшизу и зарабатывают.

Теперь я жду твой ответ на задание. После этого я дам тебе доступ ко второму уроку.

Чтобы выполнить задание, нажми на кнопку ниже 👇"""

TASK_2_PRESENTATION_DESCRIPTION = """Поздравляю тебя с прохождением первого шага🥳

Ты уже стал на 1 шаг ближе к своим мечтам.

Не затягивай и продолжай в том же темпе👏🏻 Дальше ещё интереснее

Урок 2. Мышление

🙏 Пожалуйста, не откладывай на потом эту задачу, выдели для себя время и посмотри новый урок прямо сейчас.

На этом уроке ты узнаешь с каким мышлением люди делают крутые результаты и сможешь эти знания применить в своей жизни. Мышление миллионеров можно перенять, это проще, чем ты думаешь. Отсюда и твой результат - ближе, чем может казаться на первый взгляд.

Жми на кнопку ниже, чтобы перейти ко второму уроку👇"""

TASK_2_DESCRIPTION = """Поздравляю тебя с просмотром второго урока🥳

Главная задача на этом этапе - дать тебе понимание, люди с каким мышлением создают миллионные бизнес-системы. И что ты тоже можешь, применив эти простые правила, изменить свою жизнь. Думаю, ты обратил внимание на то, какие преображения происходят у людей в нашей команде? Это то, что ждёт и тебя. Скорее проходи все шаги.

Жду твой ответ на задание и дам доступ к третьему уроку.

Чтобы выполнить задание, жми кнопку👇"""

TASK_3_PRESENTATION_DESCRIPTION = """Поздравляю с прохождением второго шага🥳

Ты уже стал на 2й шаг ближе к своему доходу в 100 тыс руб и выше🤩 Только представь. Как изменится твоя жизнь с таким доходом? А дальше х2, х3 и без ограничений
Урок 3. Компания. Структура заработка на мини-франшизе с 0 на доходность от 100 тыс руб

 
На этом уроке ты узнаешь как выбрать компанию партнера. Пошаговый план выхода на доход от 100 тыс руб и выше, понятно и прозрачно. Узнаешь как и с чего тебе начать и выйти на свой первый доход быстро. 

Жми на кнопку ниже, чтобы перейти к третьему уроку👇"""

TASK_3_DESCRIPTION = """Поздравляю тебя с просмотром 3-го самого важного урока🥳

Теперь ты можешь запустить свою мини-франшизу на официальном сайте компании Oriflame. Сразу после этого у тебя будет доступ в свой кабинет. Тебя добавят в чат, где ты познакомишься с командой.

Заполняй небольшую анкету и наставник скоро с тобой свяжется!"""

# Вопросы для уроков
QUESTION_1_1 = "1. Какие цели ты хочешь достичь, зарабатывая с нами?"
QUESTION_1_2 = "2. Есть ли у тебя опыт ведения бизнеса зарабатывая онлайн, если да, то какой?"
QUESTION_1_3 = "3. Куда ты потратишь свой первый миллион, заработанный на мини-франшизе?"

QUESTION_2_1 = "1. Сколько времени ты готов выделять на старте своего дела?"
QUESTION_2_2 = "2. В каком квадранте ты сейчас находишься? (Работаешь в найме? Своё дело? Есть свой бизнес?)"
QUESTION_2_3 = "3. Какой доход ты планируешь получать на мини-франшизе? (Какая сумма тебе была бы комфортна для жизни?)"

QUESTION_3_1 = "1. Напишите вашу Фамилию, Имя и Отчество."
QUESTION_3_2 = "2. Ваш номер телефона:"
QUESTION_3_3 = "3. Ваша электронная почта:"
QUESTION_3_4 = "3. Из какого вы города?"
QUESTION_3_5 = "3. Кто вас пригласил?"

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScsgfixaRPalMX6Iqmp72hqBipDZeEZQHq6KgkMaKsN2LoafA/viewform?usp=header"




