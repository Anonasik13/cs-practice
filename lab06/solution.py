def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]                 # имя файла без каталогов
        ext = name.rsplit(".", 1)[1].lower() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes < 1024:
        return f"{n_bytes} {units[0]}"
    for k in range(1, len(units)):
        if n_bytes < 1024 ** (k + 1):
            return f"{n_bytes / 1024 ** k:.1f} {units[k]}"
    return f"{n_bytes / 1024 ** 4:.1f} {units[4]}"     # всё, что больше ТБ

