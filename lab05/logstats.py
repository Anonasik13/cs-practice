import re

def parse_event(line: str) -> dict:
    """
    Разбирает строку журнала на составляющие: время, уровень, сообщение.
    Возвращает словарь или возбуждает ValueError для негодных строк.
    Сообщение делится не больше чем на три части через пробелы.
    """
    if not isinstance(line, str):
        raise ValueError("Строка должна быть типа str")
    
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    # Делим строку максимум на 3 части: время, уровень, сообщение
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Неполная строка журнала")
    
    time_str, level, message = parts
    
    # Проверка формата времени через регулярное выражение (YYYY-MM-DDTHH:MM:SS)
    time_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
    if not re.match(time_pattern, time_str):
        raise ValueError("Неверный формат времени")
    
    # Допустимые уровни логирования
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень лога: {level}")
        
    return {
        "time": time_str,
        "level": level,
        "message": message
    }


def count_levels(lines) -> dict:
    """
    Подсчитывает количество строк каждого уровня.
    Испорченные строки или ошибки парсинга учитываются под ключом BROKEN.
    Пустые строки пропускаются.
    """
    counts = {}
    for line in lines:
        if not line or not line.strip():
            continue
        try:
            event = parse_event(line)
            lvl = event["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts


def top_errors(lines, n: int) -> list:
    """
    Возвращает n самых частых сообщений уровня ERROR в виде пар [сообщение, сколько раз].
    При равенстве частоты — сортировка по алфавиту сообщений.
    """
    error_counts = {}
    for line in lines:
        if not line or not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
            
    # Сортируем: сначала по убыванию частоты (-count), затем по алфавиту сообщения (msg)
    sorted_errors = sorted(error_counts.items(), key=lambda item: (-item[1], item[0]))
    
    # Превращаем кортежи в списки и берём первые n элементов
    result = [[msg, cnt] for msg, cnt in sorted_errors[:n]]
    return result


def format_report(counts: dict, errors: list) -> str:
    """
    Формирует текст отчёта по готовым подсчётам.
    Уровни выводятся по алфавиту, ошибки через длинное тире «—», в конце перевод строки.
    """
    report_lines = ["Отчёт по журналу", ""]
    
    # Уровни сортируем по алфавиту
    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")
        
    report_lines.append("")
    report_lines.append("Частые ошибки:")
    
    for msg, count in errors:
        report_lines.append(f"- {msg} — {count}")
        
    return "\n".join(report_lines) + "\n"