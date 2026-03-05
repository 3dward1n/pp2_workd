"""
PYTHON CHEAT SHEET: JSON, ITERATORS, GENERATORS, SCOPES (LEGB)
============================================================
"""

import json

# --- 1. ОБЛАСТИ ВИДИМОСТИ (SCOPES / LEGB) ---
# Global (G): Видна во всем файле
VERSION = "1.0.0" 

def scope_demonstration():
    # Enclosing (E): Внешняя функция для вложенной функции
    outer_var = "Я из внешней функции"
    
    def inner_function():
        # Local (L): Видна только здесь
        local_var = "Я локальная"
        
        # Python ищет переменные по порядку: L -> E -> G -> B (Built-in)
        print(f"Доступ к L: {local_var}")
        print(f"Доступ к E: {outer_var}")
        print(f"Доступ к G: {VERSION}")
        print(f"Доступ к B: {len([1,2,3])}") # len - это Built-in
        
    inner_function()


# --- 2. ИТЕРАТОРЫ И ГЕНЕРАТОРЫ ---
# Генератор — это функция, которая не умирает после возврата значения, 
# а "засыпает" на ключевом слове yield.

def data_generator(limit):
    """
    Это ГЕНЕРАТОР. Он не хранит все данные в памяти, 
    а создает их по одному по запросу.
    """
    n = 1
    while n <= limit:
        # Вместо return используем yield
        yield {"id": n, "status": "active", "value": n * 10}
        n += 1

# Использование:
# my_gen — это ИТЕРАТОР. У него можно вызывать next()
my_gen = data_generator(3)


# --- 3. JSON (СЕРИАЛИЗАЦИЯ) ---
# Модуль json превращает объекты Python в строку (текст) и наоборот.

def json_example():
    # Создаем данные через наш генератор
    raw_data = list(data_generator(2)) # Превращаем генератор в обычный список
    
    # Python Dict -> JSON String (Сериализация)
    # indent=4 делает текст красивым (с отступами)
    json_string = json.dumps(raw_data, indent=4)
    print("\n--- JSON String ---")
    print(json_string)
    
    # JSON String -> Python Dict (Десериализация)
    parsed_data = json.loads(json_string)
    print(f"\nТип после loads: {type(parsed_data)}")


# --- ЗАПУСК ВСЕГО ВМЕСТЕ ---
if __name__ == "__main__":
    print("=== 1. ТЕСТИРУЕМ ОБЛАСТИ ВИДИМОСТИ ===")
    scope_demonstration()

    print("\n=== 2. ТЕСТИРУЕМ ГЕНЕРАТОР (ИТЕРАЦИЯ) ===")
    # Цикл for сам вызывает next() у итератора/генератора
    for item in data_generator(3):
        print(f"Получен объект: {item}")

    print("\n=== 3. ТЕСТИРУЕМ JSON ===")
    json_example()

"""
КРАТКИЙ ИТОГ (ДЛЯ ЗАПОМИНАНИЯ):
1. JSON: dumps (в строку), loads (из строки). dump/load — для файлов.
2. Итератор: Объект, который выдает элементы по одному (next()).
3. Генератор: Функция с 'yield'. Самый простой способ сделать итератор. Экономит RAM.
4. LEGB: Порядок поиска имен (Local -> Enclosing -> Global -> Built-in).
"""