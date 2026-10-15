def parse_record(line: str) -> dict:
    if not line.strip():
        raise ValueError("empty line")

    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("wrong number of fields")

    city, temp_str, date = parts

    if not city.strip():
        raise ValueError("empty city")

    if not date.strip():
        raise ValueError("empty date")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("temperature is not a number")

    return {"city": city.strip(), "temp": temp, "date": date.strip()}


def read_valid(lines: list) -> list:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            valid_records.append(parse_record(line))
        except ValueError:
            continue # 5125
    return valid_records


def average_by_city(records: list) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temp"]
        total[city] = total.get(city, 0.0) + temp
        count[city] = count.get(city, 0) + 1
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages


def warmest_city(records: list) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    best = None
    for city in sorted(averages):
        if best is None or averages[city] > averages[best]:
            best = city
    return best

