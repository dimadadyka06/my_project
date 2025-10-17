# 1. Декоратор логирования
def logger(func):
    def wrapper(*args, **kwargs):
        # Перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")

        # Выполнение функции
        result = func(*args, **kwargs)

        # После выполнения функции
        print(f"Функция {func.__name__} вернула {result}")
        return result

    return wrapper


# Применение декоратора к функциям
@logger
def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b


@logger
def divide(a, b):
    """Возвращает результат деления"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


@logger
def greet(name):
    """Выводит приветствие"""
    return f"Привет, {name}!"


# 2. Декоратор доступа
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None

        return wrapper

    return decorator


# Пример использования декоратора доступа
@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "success"


@require_role(["admin", "manager"])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "settings_updated"


@require_role(["user", "admin", "manager"])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "data_viewed"


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование декоратора логирования ===")

    # Тестирование функции add
    print("\n1. Тестирование add(5, 3):")
    result1 = add(5, 3)

    print("\n2. Тестирование add(a=10, b=20):")
    result2 = add(a=10, b=20)

    # Тестирование функции divide
    print("\n3. Тестирование divide(10, 2):")
    result3 = divide(10, 2)

    print("\n4. Тестирование divide(5, 0):")
    result4 = divide(5, 0)

    # Тестирование функции greet
    print("\n5. Тестирование greet('Анна'):")
    result5 = greet('Анна')

    print("\n=== Тестирование декоратора доступа ===")

    # Создание пользователей с разными ролями
    users = [
        {"name": "димка", "role": "admin"},
        {"name": "артем", "role": "manager"},
        {"name": "саша", "role": "user"},
        {"name": "маргарита", "role": "guest"}
    ]

    # Тестирование функций с разными пользователями
    for user in users:
        print(f"\n--- Тестирование для пользователя: {user['name']} (роль: {user['role']}) ---")

        print("Попытка удалить базу данных:")
        delete_database(user)

        print("Попытка изменить настройки:")
        edit_settings(user)

        print("Попытка просмотреть данные:")
        view_data(user)
