# File transfer api
Проект для сохранения и обработки файлов посредством Django Rest Framework

## Установка и запуск
Клонируйте репозиторий

Активируйте виртуальное окружение

Перейдите в папку с зависимостями ```requrements.txt``` командой `cd file_transfer_api/`

Установите зависимости в виртуальное окружение ```pip install -r requirements.txt```

Запустите сервер командой ```python manage.py runserver```

Запустите docker контейнер для брокера Redis ```docker run -d -p 6379:6379 redis```

Запустите celery  ```celery -A file_transfer_api worker -l INFO```

### Примеры использования API 
```/api/files/``` метод ```GET```
Получить данные о всех загруженных файлах

```/api/upload/``` метод ```POST```
Загрузить файл на сервер


# TO DO:
доделать контейнеризацию и автоматизацию запуска через ```docker-compose```
