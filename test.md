# IP History

## Web Api

### Поиск по всей истории

**`GET /<value:str>/
GET /<value:str>/?offset=<offset:int>&limit=<limit:int>`**

    <value:str> - значение объекта
    <offset:int> - с какой записи вернуть значения
    <limit:int> - максимальное  кол-во возвращаемых записей

Response:
```js
{
    "status": <status:bool>, // статус 0 или 1 тип int
    "total": <total:int>, // количество объектов
    "result": [ // список объектов
        {
            "id": <id:int>, // id объекта
            "type": "<type:str>", // тип объекта
            "value": "<value:str>", // значение объекта
            "data": [
                {"<key:str>": "<value:str>"},
                {"<key:str>": "<value:str>"},
                {
                    "<key:array>": [
                        {"<key:str>": "<value:str>"},
                        {"<key:str>": "<value:str>"},
                        ...
                    ]
                },
                ...
            ],
            "date": "<date:datetime>"
        },
        {
            "id": <id:int>,
            "type": "<type:str>",
            "value": "<value:str>",
            "data": [
                {"<key:str>": "<value:str>"},
                {"<key:str>": "<value:str>"},
                ...
            ],
            "date": "<date:datetime>"
        },
        ...
    ]
}
```

### Получение истории объекта по значению

**`GET /get/<type:str>/<value:str>/  
GET /get/<type:str>/<value:str>/<datefrom:datetime>/  
GET /get/<type:str>/<value:str>/<datefrom:datetime>/<dateto:datetime>

    <type:str> - тип объекта
    <value:str> - значение объекта
    <datefrom:datetime> - дата от
    <dateto:datetime> - дата до
    ?<offset:int> - кол-во строк перед началом вывода, default: 0
    ?<limit:int> - максимальное кол-во возвращаемых записей  default: 0

Response:
```js
{
    "status": <status:bool>, // статус 0 | 1 тип int
    "total": <total:int>, // количество объектов
    "result": [ // список объектов
        {
            "id": <id:int>, //id объекта
            "type": "<type:str>", // тип объекта
            "value": "<value:str>",
            "data": [
                {"<key:str>": "<value:str>"},
                {"<key:str>": "<value:str>"},
                {
                    "<key:array>": [
                        {"<key:str>": "<value:str>"},
                        {"<key:str>": "<value:str>"},
                        ...
                    ]
                },
                ...
            ],
            "date": "<date:datetime>"
        },
        {
            "id": <id:int>,
            "type": "<type:str>",
            "value": "<value:str>",
            "data": [
                {"<key:str>": "<value:str>"},
                {"<key:str>": "<value:str>"},
                ...
            ],
            "date": "<date:datetime>"
        },
        ...
    ]
}
```

### Добавление объекта в историю

POST /add/

Request:

```js
[
    {"<key:str>": "<value:str>"},
    {"<key:str>": "<value:str>"},
    {
        "<key:array>": [
            {"<key:str>": "<value:str>"},
            ...
         ]
    },
    ...
]

```

    <type:str> - тип объекта
    <value:str> - название объекта
    <key:str> - название объекта
    <key:array> - массив объектов


Response:

```js
{
    "status": <status:int> // статус 0 или 1
}
```

### Поставить объект на мониторинг

POST /monitoring/add/

Request:

```js
[
    {
        "type": "<type:str>",
        "value": "<value:str>"
    },
    {
        "type": "<type:str>",
        "value": "<value:str>"
    },
    ...
]

```

    <type:str> - тип объекта
    <value:str> - название объекта

Response:

```js
[
    {
        "status": <status:int>,
    },
    {
        "status": <status:int>,
    },
    ...
]
```

### Удалить объект с мониторинга

POST /monitoring/delete/<type:str>/<value:str>/


Response:

```js
[
    {
        "status": <status:int>,
    },
    {
        "status": <status:int>,
    },
    ...
]
```