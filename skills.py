import os
import webbrowser
import sys
import subprocess
import pyttsx3
# import voice

try:
    import requests  # pip install requests
except:
    pass

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://www.youtube.com', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        subprocess.Popen(
            'C:/Users/сулпак/AppData/Roaming/.minecraft/TLauncher.exe')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    # os.system('shutdown \s')
    print('пк был выключен')


def weather():
    '''Для работы этого кода нужно зарегистрироваться на сайте
    https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:
        params = {'q': 'Astana', 'units': 'metric',
                  'lang': 'ru', 'appid': 'ffa159b4b91fa748f9bd20336c3b8672'}
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(
            f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        speaker(
            'Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
