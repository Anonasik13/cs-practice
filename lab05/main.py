from logstats import count_levels, top_errors, format_report, parse_event

def main():
    # 1. Читаем имя файла журнала из первой строки ввода
    filename = input().strip()
    
    # Для корректного подсчета общего числа разобранных строк, 
    # посчитаем успешно разобранные + BROKEN (или общее число непустых строк, прошедших обработку).
    # По условию main печатает:
    # 1. сколько строк разобрано всего (успешно);
    # 2. сколько из них уровня ERROR;
    # 3. сколько испорченных.
    
    total_parsed = 0
    error_count = 0
    broken_count = 0
    
    # Делаем первый проход для подсчета статистики для вывода в консоль
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                event = parse_event(line)
                total_parsed += 1
                if event["level"] == "ERROR":
                    error_count += 1
            except ValueError:
                broken_count += 1

    # Печатаем требуемые три числа в консоль
    print(total_parsed)
    print(error_count)
    print(broken_count)
    
    # Делаем второй проход (или используем собранные данные) для формирования отчёта
    # Функции count_levels и top_errors принимают итерируемый объект (файл), 
    # поэтому передаем файл повторно, открыв его через with для экономии памяти.
    with open(filename, encoding="utf-8") as f_counts:
        counts = count_levels(f_counts)
        
    with open(filename, encoding="utf-8") as f_errors:
        errors = top_errors(f_errors, 3) # Топ-3 частых ошибок для отчёта
        
    report_text = format_report(counts, errors)
    
    # Записываем отчёт в report.txt рядом с собой в кодировке UTF-8
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()

