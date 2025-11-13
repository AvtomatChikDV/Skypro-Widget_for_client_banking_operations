import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_dates):
    """Функция проверки сортировки стандартных данных по значениям state CANCELED/EXECUTED"""
    assert filter_by_state(sample_dates) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert filter_by_state(sample_dates, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]

def test_filter_by_state_no_list():
    """Функция проверки программы при отсутствии данных"""
    assert filter_by_state([], "EXECUTED") == []

def test_filter_by_state_other_(sample_dates):
    """Функция проверки фильтрации данных при вводе нестандартного state"""
    assert filter_by_state(sample_dates, "OTHER") == []


def test_sort_by_date(operations):
    """Тест сортировки по убыванию даты (по умолчанию)"""

    result = sort_by_date(operations)

    expected_dates = ['2023-03-01T10:00:00.000000', '2023-02-01T10:00:00.000000', '2023-02-01T10:00:00.000000', '2023-01-01T10:00:00.000000']
    actual_dates = [op['date'] for op in result]

    assert actual_dates == expected_dates

    result = sort_by_date(operations, reverse=False)

    expected_dates = ['2023-01-01T10:00:00.000000', '2023-02-01T10:00:00.000000', '2023-02-01T10:00:00.000000', '2023-03-01T10:00:00.000000']
    actual_dates = [op['date'] for op in result]

    assert actual_dates == expected_dates


def test_sort_by_date_with_same_dates(operations):
    """Тест сортировки при одинаковых датах (должна сохраняться исходная порядок)"""

    result = sort_by_date(operations)

    # При одинаковых датах порядок должен сохраниться как в исходном списке
    expected_ids = [2, 3, 4, 1]
    actual_ids = [op['id'] for op in result]

    assert actual_ids == expected_ids


def test_sort_by_date_empty_list():
    """Тест сортировки пустого списка"""
    operations = []

    result = sort_by_date(operations)

    assert result == []


def test_sort_by_date_single_element():
    """Тест сортировки списка с одним элементом"""
    assert sort_by_date([{'id': 1, 'date': '2023-01-01T10:00:00.000000'}]) == [{'id': 1, 'date': '2023-01-01T10:00:00.000000'}]


def test_sort_by_date_missing_date_field():
    """Тест обработки отсутствующего поля date"""

    with pytest.raises(KeyError):
        sort_by_date([{'id': 2, 'state': 'EXECUTED'}])


