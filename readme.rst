Checker
=======

Проверка вложености скобок

Установка
---------

| В директории проекта
| Инсталяция необходимых зависимостей:

::

    $ virtualenv --prompt='(checker) ' .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

Запуск
------

В директории проекта

::

    $ python checker.py


Тестирование
------------

::

    $ nosetest
    $ nosetests --with-coverage

