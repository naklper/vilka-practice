# Вилка

Сервис поиска ресторанов и бронирования столиков.

## О проекте

"Вилка" - сайт, где пользователь может найти ресторан, посмотреть меню
и забронировать столик. Администратор добавляет рестораны и блюда,
а также подтверждает брони.

## Стек

- Python 3.14
- Django 6.1
- SQLite

## Установка и запуск

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/