import random
from collections import Counter


answer= int(input('введи номер задания (1-5)'))
if answer==1:
    print("Таблица умножения:")
    print("   ", end="")
    for i in range(1, 10):
        print(f"{i:4}", end="")
    print("\n" + "-" * 40)
    for i in range(1, 10):
        print(f"{i:2} |", end="")
        for j in range(1, 10):
            print(f"{i*j:4}", end="")
        print()


    sum_odd = 0
    for i in range(1, 101, 2):
        sum_odd += i
    print(f"Сумма всех нечётных чисел от 1 до 100: {sum_odd}")


    n = int(input("Введите число: "))
    print(f"Делители числа {n}: ", end="")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()


    n = int(input("Введите число для вычисления факториала: "))
    factorial = 1
    if n < 0:
        print("Факториал отрицательного числа не определен")
    elif n == 0:
        print("0! = 1")
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f"{n}! = {factorial}")



    n = int(input("Введите длину последовательности Фибоначчи: "))
    if n <= 0:
        print("Длина должна быть положительным числом")
    elif n == 1:
        print("0")
    else:
        a, b = 0, 1
        print("Последовательность Фибоначчи:", end=" ")
        print(a, end=" ")

        for i in range(2, n + 1):
            print(b, end=" ")
            a, b = b, a + b
        print()

if answer==2:
    # 0. Подготовка цикла из случайных чисел
    print("0. ИСХОДНЫЙ СПИСОК СЛУЧАЙНЫХ ЧИСЕЛ")
    numbers = [random.randint(-50, 50) for _ in range(10)]
    print(f"Исходный список: {numbers}")

    # 1. Вывести только чётные элементы
    print("1. ЧЁТНЫЕ ЭЛЕМЕНТЫ СПИСКА")
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Чётные элементы: {even_numbers}")

    # 2. Найти максимальное и минимальное число
    print("2. МАКСИМАЛЬНОЕ И МИНИМАЛЬНОЕ ЧИСЛО")
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print(f"Максимальное число: {max_num}")
    print(f"Минимальное число: {min_num}")

    # 3. Запросить 5 чисел у пользователя, сохранить и отсортировать
    print("3. СПИСОК ЧИСЕЛ ОТ ПОЛЬЗОВАТЕЛЯ")
    user_numbers = []
    for i in range(5):
        try:
            num = int(input(f"Введите число {i + 1}: "))
            user_numbers.append(num)
        except ValueError:
            print("Пожалуйста, введите целое число!")
            num = int(input(f"Введите число {i + 1}: "))
            user_numbers.append(num)

    user_numbers.sort()
    print(f"Отсортированный список: {user_numbers}")

    # 4. Удалить дубликаты из списка (без использования множеств)
    print("4. УДАЛЕНИЕ ДУБЛИКАТОВ ИЗ СПИСКА")
    numbers_with_duplicates = numbers.copy() + [random.choice(numbers) for _ in range(3)]
    print(f"Список с дубликатами: {numbers_with_duplicates}")

    unique_numbers = []
    for num in numbers_with_duplicates:
        if num not in unique_numbers:
            unique_numbers.append(num)

    print(f"Список без дубликатов: {unique_numbers}")

    # 5. Поменять местами первый и последний элемент
    print("5. ОБМЕН ПЕРВОГО И ПОСЛЕДНЕГО ЭЛЕМЕНТА")
    print(f"Исходный список: {numbers}")

    if len(numbers) >= 2:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
        print(f"После обмена: {numbers}")
    else:
        print("Список слишком короткий для обмена элементов")




if answer==3:
    # 1. Словарь студентов и средний балл
    print("1. СЛОВАРЬ СТУДЕНТОВ И СРЕДНИЙ БАЛЛ")

    students = {
        "Иванов": 4.5,
        "Петров": 3.8,
        "Сидорова": 4.9,
        "Козлов": 4.2,
        "Смирнова": 3.5
    }

    print("Оценки студентов:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    # Вычисляем средний балл
    total = sum(students.values())
    average = total / len(students)
    print(f"\nСредний балл: {average:.2f}")

    # 2. Подсчет букв в строке
    print("2. ПОДСЧЕТ БУКВ В СТРОКЕ")

    text = input("Введите строку для анализа: ").lower()  # Приводим к нижнему регистру

    letter_count = {}
    for char in text:
        if char.isalpha():  # Считаем только буквы
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    print("\nКоличество каждой буквы:")
    for letter, count in sorted(letter_count.items()):
        print(f"'{letter}': {count}")

    # 3. Словарь чисел и их квадратов
    print("3. СЛОВАРЬ ЧИСЕЛ И ИХ КВАДРАТОВ")

    squares_dict = {}
    for i in range(1, 11):
        squares_dict[i] = i ** 2

    print("Числа и их квадраты:")
    for number, square in squares_dict.items():
        print(f"{number}² = {square}")

    # 4. Создание словаря из двух списков
    print("4. СЛОВАРЬ ИЗ ДВУХ СПИСКОВ")

    # Списки для примера
    keys_list = ["имя", "возраст", "город", "профессия"]
    values_list = ["Анна", 25, "Москва", "инженер"]

    # Проверяем, что списки одинаковой длины
    if len(keys_list) != len(values_list):
        print("Ошибка: списки разной длины!")
    else:
        combined_dict = {}
        for i in range(len(keys_list)):
            combined_dict[keys_list[i]] = values_list[i]

        print("Созданный словарь:")
        for key, value in combined_dict.items():
            print(f"{key}: {value}")



if answer==4:
    # 1. Пересечение и объединение множеств
    print("1. ПЕРЕСЕЧЕНИЕ И ОБЪЕДИНЕНИЕ МНОЖЕСТВ")

    set1 = {1, 2, 3, 4, 5, 6}
    set2 = {4, 5, 6, 7, 8, 9}

    print(f"Множество 1: {set1}")
    print(f"Множество 2: {set2}")

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    print(f"Пересечение: {intersection}")
    print(f"Объединение: {union}")

    # 2. Уникальные слова в тексте
    print("2. УНИКАЛЬНЫЕ СЛОВА В ТЕКСТЕ")

    text = input("Введите текст: ").lower()

    # Разбиваем текст на слова, убираем знаки препинания
    words = text.split()
    unique_words = set()

    for word in words:
        # Убираем знаки препинания вокруг слова
        clean_word = word.strip('.,!?;:"()[]{}')
        if clean_word:  # Проверяем, что слово не пустое
            unique_words.add(clean_word)

    print(f"Уникальные слова: {sorted(unique_words)}")
    print(f"Количество уникальных слов: {len(unique_words)}")

    # 3. Общие элементы двух списков
    print("3. ОБЩИЕ ЭЛЕМЕНТЫ ДВУХ СПИСКОВ")

    list1 = [1, 2, 3, 4, 5, 2, 3, 1]
    list2 = [4, 5, 6, 7, 8, 4, 5]

    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")

    # Преобразуем списки в множества для удаления дубликатов
    set_from_list1 = set(list1)
    set_from_list2 = set(list2)

    common_elements = set_from_list1 & set_from_list2

    print(f"Общие элементы: {common_elements}")

    # 4. Проверка подмножества
    print("4. ПРОВЕРКА ПОДМНОЖЕСТВА")

    set_a = {1, 2, 3, 4, 5}
    set_b = {2, 3, 4}
    set_c = {6, 7, 8}

    print(f"Множество A: {set_a}")
    print(f"Множество B: {set_b}")
    print(f"Множество C: {set_c}")

    print(f"B является подмножеством A: {set_b.issubset(set_a)}")
    print(f"C является подмножеством A: {set_c.issubset(set_a)}")

    # 5. Удаление элементов меньше заданного числа
    print("5. УДАЛЕНИЕ ЭЛЕМЕНТОВ ПО УСЛОВИЮ")

    numbers_set = {10, 5, 8, 15, 3, 20, 1, 25}
    print(f"Исходное множество: {numbers_set}")

    try:
        threshold = int(input("Введите пороговое число: "))
        filtered_set = {x for x in numbers_set if x >= threshold}
        print(f"Множество после фильтрации: {filtered_set}")
    except ValueError:
        print("Ошибка! Введите целое число.")



if answer==5:
    # 1. Уникальные значения из случайного списка

    print("1. УНИКАЛЬНЫЕ ЗНАЧЕНИЯ ИЗ СЛУЧАЙНОГО СПИСКА")

    random_numbers = [random.randint(1, 15) for _ in range(20)]
    unique_numbers = list(set(random_numbers))

    print(f"Исходный список: {random_numbers}")
    print(f"Уникальные значения: {sorted(unique_numbers)}")
    print(f"Количество уникальных значений: {len(unique_numbers)}")

    # 2. Словарь частот элементов

    print("2. СЛОВАРЬ ЧАСТОТ ЭЛЕМЕНТОВ")

    frequency_dict = {}
    for num in random_numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    print("Частота элементов:")
    for num, count in sorted(frequency_dict.items()):
        print(f"{num}: {count} раз(а)")

    # 3. Множество длинных слов

    print("3. МНОЖЕСТВО ДЛИННЫХ СЛОВ")

    words = ["яблоко", "кот", "программирование", "дом", "университет", "книга",
             "компьютер", "стол", "телефон", "интернет"]

    long_words = {word for word in words if len(word) > 5}

    print(f"Исходный список слов: {words}")
    print(f"Слова длиннее 5 символов: {long_words}")

    # 4. Количество вхождений слов в предложении

    print("4. ЧАСТОТА СЛОВ В ПРЕДЛОЖЕНИИ")

    sentence = input("Введите предложение: ").lower()

    # Убираем знаки препинания и разбиваем на слова
    import string

    translator = str.maketrans('', '', string.punctuation)
    clean_sentence = sentence.translate(translator)
    words_list = clean_sentence.split()

    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Частота слов:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

    # 5. Удаление дубликатов через множество

    print("5. УДАЛЕНИЕ ДУБЛИКАТОВ ЧЕРЕЗ МНОЖЕСТВО")

    numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7, 8]
    unique_list = list(set(numbers_with_duplicates))

    print(f"Список с дубликатами: {numbers_with_duplicates}")
    print(f"Список без дубликатов: {sorted(unique_list)}")

    # 6. Самый дорогой товар

    print("6. САМЫЙ ДОРОГОЙ ТОВАР")

    products = {
        "хлеб": 50,
        "молоко": 80,
        "сыр": 300,
        "кофе": 450,
        "чай": 200,
        "шоколад": 120
    }

    most_expensive = max(products, key=products.get)
    max_price = products[most_expensive]

    print("Товары и цены:")
    for product, price in products.items():
        print(f"{product}: {price} руб.")

    print(f"\nСамый дорогой товар: {most_expensive} ({max_price} руб.)")

    # 7. Анализ повторяющихся имён

    print("7. АНАЛИЗ ПОВТОРЯЮЩИХСЯ ИМЁН")

    names = ["Анна", "Иван", "Мария", "Петр", "Анна", "Иван", "Ольга",
             "Анна", "Сергей", "Мария", "Иван", "Анна"]

    # Имена, встречающиеся более одного раза
    duplicate_names = {name for name in names if names.count(name) > 1}

    # Самое частое имя
    name_counter = Counter(names)
    most_common_name, most_common_count = name_counter.most_common(1)[0]

    print(f"Список имён: {names}")
    print(f"Имена, встречающиеся более 1 раза: {duplicate_names}")
    print(f"Самое частое имя: '{most_common_name}' ({most_common_count} раз(а))")

    # 8. Словарь первых вхождений символов

    print("8. СЛОВАРЬ ПЕРВЫХ ВХОЖДЕНИЙ СИМВОЛОВ")

    user_string = input("Введите строку: ")

    first_occurrence = {}
    for index, char in enumerate(user_string):
        if char not in first_occurrence:
            first_occurrence[char] = index

    print("Первые вхождения символов:")
    for char, index in sorted(first_occurrence.items()):
        print(f"'{char}': позиция {index}")