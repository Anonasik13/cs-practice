# stats.py

def parse_record(line: str) -> dict:
    """
    Разбирает одну строку. Если строка плохая — кидает ошибку ValueError.
    """
    # Если строка пустая (только пробелы) — это ошибка для этой функции,
    # но read_valid её отловит раньше. Для надежности тоже кинем ошибку.
    if not line.strip():
        raise ValueError("Пустая строка")

    parts = line.split(";")
    
    # Проверка: должно быть ровно 3 части
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: ожидается 3, найдено {len(parts)}")

    city, temp_str, date = parts

    # Проверка: город и дата не должны быть пустыми
    if not city.strip():
        raise ValueError("Город не может быть пустым")
    if not date.strip():
        raise ValueError("Дата не может быть пустой")

    # Проверка: температура должна быть числом
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{temp_str}'")

    return {"city": city.strip(), "temp": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> list[dict]:
    """
    Проходит по всем строкам. 
    Пустые строки игнорирует.
    Строки с ошибками пропускает (не падает).
    Возвращает только хорошие записи.
    """
    valid_records = 
    for line in lines:
        # Пустые строки пропускаем молча (не считаем за ошибку здесь)
        if not line.strip():
            continue
        
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Если parse_record кинул ошибку — значит строка битая.
            # Мы её просто пропускаем и идем дальше.
            continue
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Считает среднюю температуру по каждому городу.
    Округляет до 1 знака после запятой.
    """
    total = {}
    count = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temp"]
        
        total[city] = total.get(city, 0.0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}
    for city in total:
        avg = total[city] / count[city]
        averages[city] = round(avg, 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Находит город с самой высокой средней температурой.
    Если температуры равны — возвращает город, который первый по алфавиту.
    Если записей нет — возвращает пустую строку.
    """
    if not records:
        return ""

    averages = average_by_city(records)
    
    # Сортируем города:
    # 1. По средней температуре (убывание -> минус перед значением)
    # 2. По названию города (возрастание -> обычный порядок)
    # x - это город, x - это температура [1](https://100points.ru/wiki/math/ponyatie-predela-funktsii-i-ego-svoistva-base/)
    sorted_cities = sorted(averages.items(), key=lambda x: (-x, x)) [1](https://100points.ru/wiki/math/ponyatie-predela-funktsii-i-ego-svoistva-base/)
    
    # Возвращаем только название города (первый элемент кортежа)
    return sorted_cities
