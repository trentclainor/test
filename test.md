# IP History

## Web Api

### Поиск по всей истории

**`GET /<name:str>/`**  
**`GET /<name:str>/?offset=<offset:int>&limit=<limit:int>`**

Request:

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
            "name": "<value:str>", // название объекта
            "data": [ //
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

**`GET /get/<type:str>/<name:str>/`**  
**`GET /get/<type:str>/<name:str>/?out[]=key1&out[]=key2&offset=<offset:int>&limit=<limit:int>`**  
**`GET /get/<type:str>/<name:str>/<datefrom:datetime>/`**  
**`GET /get/<type:str>/<name:str>/<datefrom:datetime>/<dateto:datetime>/`**

Request:

    <type:str> - тип объекта
    <name:str> - название объекта
    <datefrom:datetime> - дата начала среза истории
    <dateto:datetime> - дата окончания среза
    <out:array> - массив параметров, которые надо получить, исключая другие
    <offset:int> - кол-во строк перед началом вывода, default: 0
    <limit:int> - максимальное кол-во возвращаемых записей  default: 0

Response:
```js
{
    "status": <status:bool>, // статус 0 | 1 тип int
    "total": <total:int>, // количество объектов
    "result": [ // список объектов
        {
            "id": <id:int>, //id объекта
            "type": "<type:str>", // тип объекта
            "name": "<name:str>", // значение объекта
            "data": [
                {"<key:str>": "<value:str>", ...},
                {"<key:str>": "<value:object>", ...},
                {
                    "<key:array>": [
                        {"<key:str>": "<value:str>", ...},
                        {"<key:str>": "<value:object>", ...},
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
            "name": "<name:str>",
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

**`POST /add/`**

Request:

```js
[
    {
        "type": "<type:str>", // тип объекта
        "name": "<name:str>", // название объекта
        "data": [
            {"<key:str>": "<value:str>", ...},
            {
                "<key:array>": [ // массив объектов
                    {"<key:str>": "<value:str>", ..},
                    ...
                    ]
            },
        ]
    }
    ...
]
```

    <type:str> - тип объекта
    <name:str> - название объекта
    <data:array> - массив объектов для добавления


Response:

```js
{
    "status": <status:int> // статус 0 или 1
}
```

**`POST /add/<type:str>/<name:str>/`**

    <type:str> - тип объекта
    <name:str> - название объекта

Request:

```js
[
    {"<key:str>": "<value:str>", ...},
    {
        "<key:array>": [ // массив объектов
            {"<key:str>": "<value:str>", ..},
            ...
         ]
    },
    ...
]
```


Response:

```js
{
    "status": <status:int> // статус 0 или 1
}
```

### Поставить объект на мониторинг

**`POST /monitoring/add/`**

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
    <name:str> - название объекта

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

**`POST /monitoring/add/<type:str>/<name:str>/`**

    <type:str> - тип объекта
    <name:str> - название объекта

Response:

```js
{
    "status": <status:int>,
}
```

### Удалить объект с мониторинга

**`POST /monitoring/delete/`**

Request:

```js
[
    {
        "type": "<type:str>", // тип объекта
        "name": "<name:str>" // название объекта
    },
    {
        "type": "<type:str>",
        "name": "<name:str>"
    },
    ...
]
```

    <type:str> - тип объекта
    <name:str> - название объекта

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

**`POST /monitoring/delete/<type:str>/<name:str>/`**

    <type:str> - тип объекта
    <name:str> - название объекта

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

### Статус объекта мониторинга

**`POST /monitoring/status/`**

Request:

```js
[
    {
        "type": "<type:str>", // тип объекта
        "value": "<value:str>" // название объекта
    },
    {
        "type": "<type:str>",
        "value": "<value:str>"
    },
    ...
]
```

    <type:str> - тип объекта
    <name:str> - название объекта

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

**`POST /monitoring/status/<type:str>/<value:str>/`**


Response:

```js
{
    "status": <status:int>,
}
```
