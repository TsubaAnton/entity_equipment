REST API интерфейс для работы с сущностью "оборудование".

Это приложение предоставляет REST API для работы с сущностью «Оборудование» и одностраничное SPA на Nuxt.js для взаимодействия с API.

Технические требования: Backend: Python 3.10+ Django 4.2 DRF 3.10+ MySQL Frontend: Nuxt.js 3 Vue 3 Tailwind CSS Axios

Перед запуском web-приложения необходимо:

Создать базу данных MySQL (Например, через команду CREATE DATABASE equipment_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;)
Создать и применить миграции (cd config и python manage.py migrate)
Установить все необходимые пакеты из requirements.txt (pip install -r requirements.txt)
Заполнить файл .env в соответствии с файлом env.sample
Используйте команду 'python manage.py create_test_data', чтобы создать типы оборудования
Используйте команду 'python manage.py createsuperuser', чтобы создать суперпользователя
Запуск сервера разработки: перейдите в директорию config и введите команду python manage.py runserver Запуск frontend: перейдите в директорию frontend и введите команду npm run dev

Документация доступна по адресу: http://localhost:8000/swagger/ http://localhost:8000/redoc/
