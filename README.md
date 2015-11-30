# IP History

## Web Api

### Получение истории объекта по значению

**`GET /<name:str>/`**  
**`GET /<name:str>/?out[]=key1&out[]=key2&offset=<offset:int>&limit=<limit:int>`**  
**`GET /<name:str>/?offset=<offset:int>&limit=<limit:int>`**  
**`GET /<type:str>/<name:str>/`**  
**`GET /<type:str>/<name:str>/?out[]=key1&out[]=key2&offset=<offset:int>&limit=<limit:int>`**  
**`GET /<type:str>/<name:str>/<datefrom:datetime>/`**  
**`GET /<type:str>/<name:str>/<datefrom:datetime>/<dateto:datetime>/`**

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
                {
                    "<key:array>": [
                        <value:object>,
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
                {"<key:str>": "<value:str>", ...},
                {
                    "<key:array>": [
                        <value:object>,
                        ...
                    ]
                },
                ...
            ],
            "date": "<date:datetime>"
        },
        ...
    ]
}
```

### Добавление объекта в историю

**`POST /`**

Request:

```js
[
    {
        "type": "<type:str>", // тип объекта
        "name": "<name:str>", // название объекта
        "data": [
            {"<key:str>": "<value:str>", ...},
            {
                "<key:array>": [
                    <value:object>,
                    ...
                ]
            },
        ]
    },
    ...
]
```

    <type:str> - тип объекта
    <name:str> - название объекта
    <data:array> - массив объектов для добавления


Response:

```js
[
    {"status": <status:int> }, // статус 0 или 1
    {"status": <status:int>},
    ...
]
```

**`GET /add/<type:str>/<name:str>/<key:str>/<value:str:>/`**

Request:

    <type:str> - тип объекта
    <name:str> - название объекта
    <key:str> - ключ объекта
    <value:str> - значение объекта

Response:

```js
{
    "status": <status:int> // статус 0 или 1
}
```

### Поставить объект на мониторинг

**`POST /monitoring/`**

Request:

```js
[
    {
        "type": "<type:str>", // тип объекта
        "name": "<name:str>", // название объекта
        "interval": <interval:int>, // периодиочность мониторинга в секундах
        "date_to": <date_to:datetime> // дата окончания мониторинга
    },
    {
        "type": "<type:str>",
        "name": "<name:str>",
        "interval": <interval:int>
    },
    ...
]
```

Response:

```js
[
    {"status": <status:int> }, // статус 0 или 1
    {"status": <status:int>},
    ...
]
```

**`GET /monitoring/add/<type:str>/<name:str>/<interval:int>/`**  
**`GET /monitoring/add/<type:str>/<name:str>/<interval:int>/<date_to:int>/`**

Request:

    <type:str> - тип объекта
    <name:str> - название объекта
    <interval:int> - периодиочность мониторинга в секундах
    <date_to:datetime> - дата окончания мониторинга, default: 0

Response:

```js
{
    "status": <status:int>
}
```

### Удалить объект с мониторинга

**`DELETE /monitoring/`**

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

Response:

```js
[
    {"status": <status:int> }, // статус 0 или 1
    {"status": <status:int>},
    ...
]
```

**`GET /monitoring/delete/<type:str>/<name:str>/`**

Request:

    <type:str> - тип объекта
    <name:str> - название объекта

Response:

```js
{
    "status": <status:int>  // статус 0 или 1
}
```

### Статус объекта мониторинга

**`POST /monitoring/status/`**

Request:

```js
[
    {
        "type": "<type:str>", // тип объекта
        "name": "<name:str>", // название объекта
        "interval": <interval:int>, // периодиочность мониторинга в секундах
        "date_to": "<date_to:datetime>" // дата окончания мониторинга, default: 0
    },
    {
        "type": "<type:str>",
        "name": "<name:str>",
        "interval": <interval:int>
    },
    ...
]
```

    <type:str> - тип объекта
    <name:str> - название объекта
    <interval:int> - периодиочность мониторинга в секундах
    <date_to:datetime> - дата окончания мониторинга, default: 0

Response:

```js
[
    {"status": <status:int>}, // статус 0 или 1
    {"status": <status:int>},
    ...
]
```

**`GET /monitoring/status/<type:str>/<value:str>/`**

Request:

    <type:str> - тип объекта
    <name:str> - название объекта

Response:

```js
{
    "status": <status:int>  // статус 0 или 1
}
```
