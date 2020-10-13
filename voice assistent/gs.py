import speech_recognition as sr
import os
import sys
import webbrowser


# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):

    print(words) # Дополнительно выводим на экран



# Вызов функции и передача строки 
# именно эта строка будет проговорена компьютером


""" 
    Функция command() служит для отслеживания микрофона.
    Вызывая функцию мы будет слушать что скажет пользователь,
    при этом для прослушивания будет использован микрофон.
    Получение данные будут сконвертированы в строку и далее
    будет происходить их проверка.
"""
def command():
    # Создаем объект на основе библиотеки
    # speech_recognition и вызываем метод для определения данных
    r = sr.Recognizer()

    # Начинаем прослушивать микрофон и записываем данные в source
    with sr.Microphone() as source:
        # Просто вывод, чтобы мы знали когда говорить
        print("Говорите")
        # Устанавливаем паузу, чтобы прослушивание
        # началось лишь по прошествию 1 секунды
       
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)

    try: # Обрабатываем все при помощи исключений

        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        # Просто отображаем текст что сказал пользователь
        print("Вы сказали: " + zadanie)
        if zadanie=='андрей':
            os.system("python3 speech_ai1.py")
        if "открой на ivi" in zadanie:
            adress = zadanie.replace('открой на ivi','').strip()

            webbrowser.open('https://www.ivi.ru/search/?q='+adress)

            adress=''
        if "открой в браузере" in zadanie:
            adress = zadanie.replace('открой в браузере','').strip()
            webbrowser.open('https://www.google.com/search?q='+adress)
            adress=''
        if "закрой браузер" in zadanie:
           os.system("killall chromium-browse")
    # Если не смогли распознать текст, то будет вызвана эта ошибка
    except sr.UnknownValueError:
        # Здесь просто проговариваем слова "Я вас не поняла"
        # и вызываем снова функцию command() для
        # получения текста от пользователя
       
        zadanie = command()

    # В конце функции возвращаем текст задания
    # или же повторный вызов функции
    return zadanie

# Данная функция служит для проверки текста, 
# что сказал пользователь (zadanie - текст от пользователя)


# Вызов функции для проверки текста будет 
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
    command()

