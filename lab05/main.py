import sys
from logstats import count_levels, top_errors, format_report

def main():
    # Имя файла читаем из первой строки ввода (stdin)
    path = sys.stdin.readline().strip()
    if not path:
        return

    total_parsed = 0
    error_count = 0
    broken_count = 0

    # Первый проход: считаем статистику и выводим три числа
    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    total_parsed = sum(counts[lvl] for lvl in ["DEBUG", "INFO", "WARNING", "ERROR"])
    error_count = counts["ERROR"]
    broken_count = counts["BROKEN"]

    print(total_parsed)
    print(error_count)
    print(broken_count)

    # Второй проход: собираем топ ошибок и пишем отчёт
    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, 10)  # n=10 — можно поменять, если нужно другое число

    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)


if __name__ == "__main__":
    main()
    # 3


