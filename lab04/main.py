# main.py

import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    # 1. Читаем весь ввод из консоли (или файла)
    lines = sys.stdin.read().splitlines()
    
    # Считаем общее количество строк
    total_lines = len(lines)
    
    # 2. Получаем только валидные записи через нашу функцию
    valid_records = read_valid(lines)
    valid_count = len(valid_records)
    
    # Считаем количество пустых строк (они не считаются ни за успех, ни за ошибку)
    empty_count = sum(1 for line in lines if not line.strip())
    
    # Считаем количество строк с ошибками
    # Формула: Всего - Валидные - Пустые
    error_count = total_lines - valid_count - empty_count
    
    # 3. Находим самый тёплый город
    warmest = warmest_city(valid_records)
    
    # 4. Получаем его среднюю температуру
    if warmest:
        averages = average_by_city(valid_records)
        result_temp = averages[warmest]
    else:
        # Если вообще не было хороших строк
        result_temp = 0.0

    # 5. Печатаем результат строго в таком порядке:
    # Сколько записей разобрано
    print(valid_count)
    # Сколько строк пропущено из-за ошибок
    print(error_count)
    # Средняя температура самого тёплого города (1 знак после точки)
    print(f"{result_temp:.1f}")

if __name__ == "__main__":
    main()
