from decimal import Decimal, getcontext
from fractions import Fraction
from datetime import datetime, date


#1
squares = [x**2 for x in range(1, 11)]
print("список квадротов чисел от 1 до 10\n",squares)


#2
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("список только четных чисел из диапазона 1-20\n",even_numbers)


#3
words = ["python", "java", "c++", "rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print("все слова в верхнем регистре и длинее 3-х символов\n",result)


#4
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

sim = int(input("введи число"))
print("класс итератор который возвращает число от",sim," до 1")
for x in Countdown(sim):
    print(x)


#5
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("генератор фибоначи")
n1 = int(input("введи длину фибоначи: "))
print("числа фибоначи")
for num in fibonacci(n1):
    print(num, end=" ")


#6
def detailed_deposit_calculator():

    getcontext().prec = 10
    print("\n=== ДЕТАЛЬНЫЙ ФИНАНСОВЫЙ КАЛЬКУЛЯТОР ===")

    initial_amount = Decimal(input("Начальная сумма: "))
    interest_rate = Decimal(input("Годовая ставка (%): "))
    years = Decimal(input("Срок (лет): "))

    # Расчет месячной процентной ставки
    monthly_rate = interest_rate / (Decimal('12') * Decimal('100'))
    print(f"Месячная ставка: {monthly_rate:.6f}")

    months = Decimal('12') * years
    final_amount = initial_amount * ((Decimal('1') + monthly_rate) ** months)
    final_amount = final_amount.quantize(Decimal('0.01'))  # Округление до копеек

    profit = final_amount - initial_amount
    profit = profit.quantize(Decimal('0.01'))

    print("\nИТОГИ:")
    print(f"Через {years} лет:")
    print(f"Начальные инвестиции: {initial_amount} ₽")
    print(f"Итоговая сумма:       {final_amount} ₽")
    print(f"Чистая прибыль:       {profit} ₽")

detailed_deposit_calculator()



#7
fraction1 = Fraction(3, 4)
fraction2 = Fraction(5, 6)

print("Исходные дроби:")
print(f"Дробь 1: {fraction1}")
print(f"Дробь 2: {fraction2}")
print()

summa = fraction1 + fraction2
vichitanie = fraction1 - fraction2
multiplication = fraction1 * fraction2
delenie = fraction1 / fraction2

print("Результаты операций (несократимые дроби):")
print(f"Сложение: {fraction1} + {fraction2} = {summa}")
print(f"Вычитание: {fraction1} - {fraction2} = {vichitanie}")
print(f"Умножение: {fraction1} × {fraction2} = {multiplication}")
print(f"Деление: {fraction1} ÷ {fraction2} = {delenie}")


#8
current_datetime = datetime.now()

print("=== ТЕКУЩАЯ ДАТА И ВРЕМЯ ===")
print()

print("1. Текущая дата и время:")
print(f"{current_datetime.strftime('%d.%m.%Y %H:%M:%S')}")
print()

print("2. Только текущая дата:")
print(f"{current_datetime.strftime('%d.%m.%Y')}")
print()

print("3. Только текущее время:")
print(f" {current_datetime.strftime('%H:%M:%S')}")


#9
print("ВЫЧИСЛЕНИЕ РАЗНИЦЫ ДАТ ")
print()

birthday_input = input("Введите вашу дату рождения (дд.мм.гггг): ")
birthday = datetime.strptime(birthday_input, "%d.%m.%Y").date()

today = date.today()

print(f"Дата рождения: {birthday.strftime('%d.%m.%Y')}")
print(f"Сегодняшняя дата: {today.strftime('%d.%m.%Y')}")
print()

days_passed = (today - birthday).days
print(f"С момента рождения прошло: {days_passed} дней")

next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_to_birthday = (next_birthday - today).days
print(f" До следующего дня рождения: {days_to_birthday} дней")

if today.day == birthday.day and today.month == birthday.month:
    print(" С ДНЕМ РОЖДЕНИЯ! ")

#10
def format_datetime_russian(dt):

    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    day = dt.day
    month = months[dt.month]
    year = dt.year
    time = dt.strftime("%H:%M")
    return f"\nСегодня {day} {month} {year} года, время: {time}"

current_time = datetime.now()
formatted_string = format_datetime_russian(current_time)
print(formatted_string)