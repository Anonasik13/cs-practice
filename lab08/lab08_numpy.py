import numpy as np

# Практическое занятие 08: NumPy - массивы, форма, индексация и срезы 1


# ================= Задание 1. Создание векторов и матриц =================
print("=" * 60)
print("Задание 1. Создание векторов и матриц")
print("=" * 60)

# Числа от 0 до 21 с шагом 3
hours = np.arange(0, 22, 3)

# Пять равноудалённых чисел от 0 до 1 включительно
line = np.linspace(0, 1, 5)

# Вектор из шести нулей целого типа
zeros = np.zeros(6, dtype=int)

# Матрица формы (2, 3), полностью заполненная числом -1
unknown_table = np.full((2, 3), -1)

# Единичная матрица 3x3
identity = np.eye(3, dtype=int)

print("hours          =", hours)
print("hours.shape    =", hours.shape)
print("hours.ndim     =", hours.ndim)
print("hours.size     =", hours.size)
print("hours.dtype    =", hours.dtype)
print()
print("line          =", line)
print("zeros         =", zeros)
print("unknown_table =")
print(unknown_table)
print("identity      =")
print(identity)


# ================= Задание 2. Индексы и срезы в векторе =================
print()
print("=" * 60)
print("Задание 2. Индексы и срезы в векторе")
print("=" * 60)

print("hours                       =", hours)
print("Третий элемент              =", hours[2])       # индексация с нуля
print("Последний элемент           =", hours[-1])
print("Элементы с индексами 2-5    =", hours[2:6])     # правая граница не входит
print("Каждый второй элемент       =", hours[::2])
print("Массив в обратном порядке   =", hours[::-1])


# ================= Задание 3. Строки и столбцы таблицы =================
print()
print("=" * 60)
print("Задание 3. Строки и столбцы таблицы")
print("=" * 60)

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("temperatures =")
print(temperatures)
print("Форма (shape)                  =", temperatures.shape)   # (3, 4)
print("Число измерений (ndim)         =", temperatures.ndim)   # 2
print("Число элементов (size)         =", temperatures.size)   # 12
print("Значение [строка 1, столбец 2] =", temperatures[1, 2])  # 16
print("Первая строка                  =", temperatures[0])
print("Последний столбец              =", temperatures[:, -1])
print("Первые две строки без первого столбца =")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2x2 (строки 0-1, столбцы 1-2) =")
print(temperatures[:2, 1:3])
print("Его shape:", temperatures[:2, 1:3].shape)  # (2, 2)


# ================= Задание 4. Прямоугольные срезы =================
print()
print("=" * 60)
print("Задание 4. Прямоугольные срезы")
print("=" * 60)

matrix = np.arange(1, 26).reshape(5, 5)
print("matrix =")
print(matrix)

first_three_rows = matrix[:3]
print("\nПервые три строки:")
print(first_three_rows)
print("shape:", first_three_rows.shape)

last_two_rows = matrix[-2:]
print("\nПоследние две строки:")
print(last_two_rows)
print("shape:", last_two_rows.shape)

first_two_columns = matrix[:, :2]
print("\nПервые два столбца:")
print(first_two_columns)
print("shape:", first_two_columns.shape)

block = matrix[1:4, 2:5]
print("\nФрагмент из строк 1-3 и столбцов 2-4:")
print(block)
print("shape:", block.shape)

bottom_right = matrix[-2:, -2:]
print("\nУгловой блок 2x2 в правом нижнем углу:")
print(bottom_right)
print("shape:", bottom_right.shape)


# ================= Задание 5. Изменение массива с помощью срезов =================
print()
print("=" * 60)
print("Задание 5. Изменение массива с помощью срезов")
print("=" * 60)

# Примеры из условия
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после vector[1:4] = 0 :", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix =")
print(small_matrix)

# --- Часть 1: changed_hours ---
# .copy() нужна потому, что срез NumPy НЕ создаёт новую копию данных,
# а возвращает представление (view) того же массива: changed_hours = hours
# указывало бы на те же элементы, и любые изменения через срезы меняли бы
# и исходный hours. .copy() делает настоящую независимую копию.
changed_hours = hours.copy()

# Заменяем элементы с индексами 2, 3, 4 на 99 (правая граница не входит)
changed_hours[2:5] = 99

# Каждый второй элемент, начиная с первого (индекс 0): 0, 2, 4, 6...
changed_hours[::2] = -1

print("\nchanged_hours =", changed_hours)
print("Исходный hours =", hours)

# --- Часть 2: changed_matrix ---
changed_matrix = matrix.copy()

# Всю вторую строку (индекс 1) на нули
changed_matrix[1, :] = 0

# Последний столбец (индекс 4) на -1
changed_matrix[:, -1] = -1

# Центральный блок 3x3 (строки и столбцы с индексами 1-3) на 100
changed_matrix[1:4, 1:4] = 100

print("\nchanged_matrix =")
print(changed_matrix)
print("\nИсходная matrix =")
print(matrix)


# ================= Задание 6. Изменение формы =================
print()
print("=" * 60)
print("Задание 6. Изменение формы")
print("=" * 60)

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers            =", numbers)
print("numbers.shape      =", numbers.shape)
print("table              =")
print(table)
print("table.shape        =", table.shape)
print("transposed         =")
print(transposed)
print("transposed.shape   =", transposed.shape)

# Почему reshape(3, 4) работает, а reshape(5, 3) вызовет ошибку:
# reshape возможен только когда произведение новых измерений равно числу
# элементов массива. Здесь 3 * 4 = 12 = numbers.size, поэтому reshape(3, 4)
# проходит. Для reshape(5, 3) было бы 5 * 3 = 15 != 12, и NumPy выбросил бы
# ValueError: cannot reshape array of size 12 into shape (5, 3).
