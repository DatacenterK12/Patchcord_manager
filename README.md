### Описание 
Patchcord_manager сервис предназначенный для учета потчкордов в ДЦ.

### Технологии
+ Python 3.7
+ Django 3.2
+ DRF
+ REDOC
+ SMTP

### Запуск проекта в dev-режиме
+ Клонировать репозиторий и перейти в него в командной строке.
+ Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
``` 
py -3.7 -m venv venv
```
```
venv/Scripts/activate
```
```
python -m pip install --upgrade pip 
```
Затем нужно установить все зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Выполняем миграции:
```
python manage.py migrate
```
Создаем суперпользователя:
```
python manage.py createsuperuser
```
Запускаем проект:
```
python manage.py runserver
```
### Примеры работы с API для всех пользователей
Примеры запросов и ответов API можно посмотреть после запуска проекта, на странице /REDOC
