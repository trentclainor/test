# Checker

Парсинг лога пользователей с FTP и сохранение статистики

## Установка

В директории проекта
Инсталяция необходимых зависимостей:

    $ virtualenv --prompt='(checker) ' .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt
    
Изменить FTP_URI в config.py на актуальный

## Запуск

В директории проекта

    $ python checker.py

Показать статистику

    $ python checker.py --stats
    

## Тестирование

    $ nosetest

