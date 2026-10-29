def count_by_extension(paths):
    counts = {}
    
    for path in paths:
        # Находим последнюю точку в имени файла (не в пути!)
        # Сначала отделяем имя файла от пути
        filename = path.split('/')[-1]
        
        # Логика для скрытых файлов: если файл начинается с точки и точек больше нет, расширения нет
        if filename.startswith('.') and filename.count('.') == 1:
            ext = ""
        else:
            # Ищем последнюю точку
            last_dot_index = filename.rfind('.')
            
            # Если точки нет или она в самом начале (но мы уже обработали случай с одной точкой в начале)
            if last_dot_index == -1 or last_dot_index == 0:
                ext = ""
            else:
                # Берём всё после последней точки и приводим к нижнему регистру
                ext = filename[last_dot_index + 1:].lower()
        
        counts[ext] = counts.get(ext, 0) + 1
        
    return counts
