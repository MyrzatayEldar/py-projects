import smtplib
from random import choice
from transliterate import translit
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import re


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y):
    """
    Функция отвечающая за построение 'пирога',
    то есть построение графика учета учеников и на какие курсы они ходят.
    """
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(y, labels=x,
           autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    graph = get_graph()
    return graph


def gen_login_and_pass(name, surname):
    """
    Функция предназначенная для генерации логина и пароля используя имя на русском языке.
    Интеграция с библиотекой transliterate.
    Использованная библиотека меняет мягкий знак на ' , что не очень хорошо для логина, поэтому пришлось его удалить
    если он присутствует в логине.
    """
    name = translit(name, 'ru', reversed=True)
    surname = translit(surname, 'ru', reversed=True)
    login = f'{surname}.{name}'
    if "\'" in login:
        login = login.replace("\'", "").lower()

    # генерация пароля случайным образом.
    eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
    eng_low = [i.lower() for i in eng]
    nums = [str(i) for i in range(0, 10)]
    gen = eng + eng_low + nums
    password = ''
    r = 10
    for i in range(r):
        password += choice(gen)
    return [login.lower(), password]


def send_success_mess(who, message):
    """
    Функция которая будет отправлять сообщение об успешной регистрации на платформу.
    В качестве одного единственного параметра принимает адрес почты, куда нужно отправить письмо.
    """
    # message = 'Qutty bolsyn! Siz bizdin Platformaga tirkeldiniz!'
    sender = 'eldar.myrza@gmail.com'
    password = '777eldar.2001'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, who, f'Subject: Tirkelu satti boldy!! \n{message}')

        return 'The message sent successfully!'
    except Exception as e:
        print(e)

