def filter_by_state(processing: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список операций по статусу выполнения.
    Переменная processing - список библиотек формата:
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'} и т.д.]"""
    return [item for item in processing if item["state"] == state]
