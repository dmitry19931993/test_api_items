# Реализация CRUD и авторизации на FastAPI

## Как установить
Для работы сервиса требуются:
- Python версии не ниже 3.10.
- установленное ПО для контейнеризации - [Docker](https://docs.docker.com/engine/install/).
- Инструмент [pipenv] для управления зависимостями и сборкой пакетов в Python.

Настройка переменных окружения
1. Переменные окружения находятся в файле .env_dev

Запуск СУБД Postgresql
```shell
docker-compose -f docker-compose.dev.yaml up
```

Установка и активация виртуального окружения
```shell
pip install pipenv  ; установка пакетов
pipenv shell  ; активация виртуального окружения
pipenv install --dev  ; установка всех зависимостей
```


## Как запустить web-сервер
Запуск сервера производится в активированном локальном окружение из папки `test_api_items/`
```shell
python main.py
```

# Цели проекта

Код написан в учебных целях 