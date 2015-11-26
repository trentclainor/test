IP History
==========

Web Api
-------

Поиск по всей истории
~~~~~~~~~~~~~~~~~~~~~

GET /:query/?offset=:offset&limit=:limit

| **``:query``** - строка со значением поиска
| **``:offset``** - с какой записи вернуть значения
| **``:limit``** - максимальное кол-во возвращаемых записей

Response:

.. code:: json

    {
        "status": 1, // статус 0 | 1 тип int
        "total": 100, // количество объектов тип int
        "result": [ // массив объектов тип array
            {
                "id" : ":int",
                "type": ":str",
                "type": ":str",
            },
            ...
        ]
    }

Получение истории по поисковой строке
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GET /get/:type/:value

| **``:type``** - срока
| **``:value``** - строка
| ***``:offset``*** - кол-во строк перед началом вывода
| ***``:limit``*** - максимальное кол-во возвращаемых записей

Response:

.. code:: json

    {
        "status": 1, // статус 0 | 1 тип int
        "total": 100, // количество объектов тип int
        "result": [ // массив объектов тип array
            {
                "key" : ":str",
                "value": ":str",
            },
            ...
        ]
    }

Добавление истории
~~~~~~~~~~~~~~~~~~

POST /add/

Request:

.. code:: json

    {
        "type": ":str"
        "key": "",
        "value": ""
    }

Responde:

.. code:: json

    {
        "status": 0|1
    }

POST /add/{type}/

.. code:: json

    {
        "status": 0|1
        "data" : {

        }
    }