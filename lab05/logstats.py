def parse_event(line: str) -> dict:
    """
    Разбирает строку журнала вида:
      2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv
    Возвращает: {"time": ..., "level": ..., "message": ...}
    Если строка невалидна — ValueError.
    """
    line = line.strip()
    if not line:
        raise ValueError("Empty line")

    # Ищем первые два пробела: время (до первого), уровень (между первым и вторым), остальное — сообщение
    first_space = line.find(" ")
    if first_space == -1:
        raise ValueError("No spaces")

    second_space = line.find(" ", first_space + 1)
    if second_space == -1 or second_space == len(line) - 1:
        # Нет второго пробела или он в конце — значит, нет сообщения или уровня
        raise ValueError("Missing level or message")

    time_part = line[:first_space]
    level_part = line[first_space + 1:second_space]
    message_part = line[second_space + 1:]

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level_part not in valid_levels:
        raise ValueError(f"Unknown level: {level_part}")

    return {"time": time_part, "level": level_part, "message": message_part}


def count_levels(lines):
    """
    Считает количество строк по уровням.
    lines — итерируемый объект (список строк или открытый файл).
    Негодные строки считаются под ключом BROKEN.
    Пустые строки пропускаются.
    """
    counts = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0, "BROKEN": 0}

    for line in lines:
        line = line.rstrip("\n")
        if not line.strip():
            continue  # пропускаем пустые

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] += 1

    return counts


def top_errors(lines, n: int):
    """
    n самых частых сообщений уровня ERROR.
    При равенстве частоты — сортировка по алфавиту сообщения.
    Возвращает список пар [сообщение, количество].
    """
    from collections import Counter

    error_messages = []

    for line in lines:
        line = line.rstrip("\n")
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                error_messages.append(event["message"])
        except ValueError:
            # битые строки не считаются как ошибки
            continue

    counter = Counter(error_messages)

    # сортируем: сначала по частоте (убывание), потом по сообщению (возрастание)
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    result = [[msg, cnt] for msg, cnt in sorted_items[:n]]
    return result


def format_report(counts: dict, errors: list):
    """
    Форматирует отчёт как в задании.
    Уровни выводятся по алфавиту, в конце — перевод строки.
    """
    lines_out = ["Отчёт по журналу"]

    # Уровни по алфавиту (исключая BROKEN, чтобы он был первым по условию примера)
    # Но в примере BROKEN стоит первым, поэтому сделаем так: BROKEN отдельно, остальные — по алфавиту
    levels_order = ["BROKEN", "DEBUG", "ERROR", "INFO", "WARNING"]

    for lvl in levels_order:
        if lvl in counts:
            lines_out.append(f"{lvl}: {counts[lvl]}")

    if errors:
        lines_out.append("Частые ошибки:")
        for msg, cnt in errors:
            lines_out.append(f"- {msg} — {cnt}")

    return "\n".join(lines_out) + "\n"
