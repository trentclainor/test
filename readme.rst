Checker
=======

Проверка вложености скобок

Установка
---------

| В директории проекта
| Инсталяция необходимых зависимостей:

::

    $ git clone git@github.com:trentclainor/test.git
    $ cd test
    $ git checkout -b brackets
    $ git pull origin brackets
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

