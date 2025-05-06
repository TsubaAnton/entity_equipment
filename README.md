REST API интерфейс для работы с сущностью "оборудование"

Технические требования:
Backend: Python 3.10+ Django 4.2 DRF 3.10+ MySQL
Frontend: Nuxt.js 3 Vue 3 Tailwind CSS Axios

Перед запуском web-приложения необходимо:
1. Создать базу данных MySQL
2. Создать и применить миграции
3. Установить все необходимые пакеты из requirements.txt
4. Заполнить файл .env
5. Используйте команду 'python manage.py create_test_data', чтобы создать типы оборудования
6. Используйте команду 'python manage.py createsuperuser', чтобы создать суперпользователя

Доступна по адресу:
http://localhost:8000/swagger/
http://localhost:8000/redoc/

