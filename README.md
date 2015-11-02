# Checker

Парсинг файла с FTP 

## Установка

В директории проекта
Инсталяция необходимых зависимостей:

    $ virtualenv --prompt='(checker) ' .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

## Запуск

В директории проекта

    $ python checker.py

Показать статистику

    $ python checker.py --stats
    

## Тестирование

    $ nosetest

