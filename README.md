# Задание 1: юнит-тесты Stellar Burgers

Тесты проверяют классы `Bun`, `Burger`, `Ingredient` и `Database`. Для
зависимостей `Burger` используются моки, а наборы данных для проверки цены,
чека и граничных случаев параметризованы. Каждый тест получает новые объекты
и не зависит от выполнения других тестов.

В исходном коде нет проверки пустого имени или отрицательной цены. Тесты не
ожидают исключений, которых программа не реализует.

## Структура

- `praktikum/` — код программы;
- `tests/test_bun.py`, `tests/test_burger.py`, `tests/test_ingredient.py`,
  `tests/test_database.py` — тесты соответствующих классов;
- `tests/conftest.py` — независимые фикстуры и фабрика моков;
- `main.py` — пример сборки бургера.

## Запуск

```bash
python -m pip install -r requirements.txt
python -m pytest tests --cov=praktikum --cov-report=term-missing --cov-report=html --cov-fail-under=70
```

HTML-отчёт создаётся в `htmlcov/index.html`. На текущем наборе из 25 тестов
покрытие пакета `praktikum` составляет 100% (69 из 69 строк кода).
