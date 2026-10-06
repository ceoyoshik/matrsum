"""МатрСум-11: сумма элементов столбцов матрицы с нулевым элементом.

Вариант 11: дана вещественная матрица размерности n x m. Найти общую
сумму элементов только тех столбцов, которые имеют хотя бы один
нулевой элемент.
"""

# Количество знаков после запятой при выводе результата
PRECISION = 3


def read_positive_int(prompt):
    """Запрашивает натуральное число, пока не будет введено корректное."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if value < 1:
            print("Ошибка: число должно быть не меньше 1.")
            continue
        return value


def input_matrix():
    """Вводит размерность и элементы матрицы с проверкой корректности."""
    n = read_positive_int("Введите количество строк (n): ")
    m = read_positive_int("Введите количество столбцов (m): ")
    print("Введите элементы матрицы по строкам (через пробел):")
    matrix = []
    while len(matrix) < n:
        raw = input(f"Строка {len(matrix) + 1}: ").split()
        if len(raw) != m:
            print(f"Ошибка: нужно ввести ровно {m} чисел.")
            continue
        try:
            row = [float(x) for x in raw]
        except ValueError:
            print("Ошибка: элементы должны быть числами.")
            continue
        matrix.append(row)
    return matrix


def find_zero_columns_sum(matrix):
    """Возвращает номера столбцов (с 1) с нулём и сумму их элементов."""
    columns = []
    total_sum = 0.0
    for j in range(len(matrix[0])):
        column = [row[j] for row in matrix]
        if any(x == 0 for x in column):
            columns.append(j + 1)
            total_sum += sum(column)
    return columns, total_sum


def print_results(columns, total_sum):
    """Выводит результат на экран."""
    if not columns:
        print("Столбцов с нулевым элементом не найдено.")
    else:
        print("Столбцы с нулевым элементом:", *columns)
    print(f"Общая сумма = {total_sum:.{PRECISION}f}")


def main():
    """Главная функция: ввод, вычисление, вывод, повтор по желанию."""
    while True:
        matrix = input_matrix()
        columns, total_sum = find_zero_columns_sum(matrix)
        print_results(columns, total_sum)
        answer = input("Продолжить? (д/н): ").strip().lower()
        if answer not in ("д", "y", "да", "yes"):
            break


if __name__ == "__main__":
    main()
