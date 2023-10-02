# Food_plan


## Установка
1. Установить зависимости командой
```
pip install -r requirements.txt
```
2. Создать файл `'.env'`. В него поместить секретный ключ
```
SECRET_KEY = <ваш токен>
```
3. Выполнить миграцию
```
python manage.py migrate
```
4. Создать суперпользователя
```
python manage.py createsuperuser
```
---

## Запуск админки

1. Запустить сервер разработки
```
python manage.py runserver
```
2. Перейти по адресу http://127.0.0.1:8000/admin/
---
