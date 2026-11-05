import json


def _convert(value: str):
    """Приводит строку к числу, булеву значению или оставляет строкой."""
    value = value.strip()
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(header, values)))
    return records


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None
    for line in lines:
        if "#" in line:
            line = line.split("#", 1)[0]
        line = line.rstrip()
        if not line.strip():
            continue
        if line.startswith("- "):
            if current_list is not None:
                current_list.append(_convert(line[2:]))
            continue
        current_list = None
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value == "":
            current_list = settings.setdefault(key, [])
        else:
            settings[key] = _convert(value)
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        matched = extra.get(row.get(key)) if row.get(key) is not None else None
        if isinstance(matched, dict):
            result.append({**matched, **row})
        else:
            result.append(dict(row))
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
