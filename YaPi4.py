# 1. Базовый класс Transport
class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"


# 2. Наследники
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    # 3. Магические методы
    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"


# 4. Практика использования
if __name__ == "__main__":
    print("=== Создание объектов ===")
    transport1 = Transport("Generic", 50)
    car1 = Car("Toyota", 120, 5)
    car2 = Car("Honda", 100, 4)
    bike1 = Bike("Giant", 25, "sport")

    print(transport1)
    print(car1)
    print(car2)
    print(bike1)
    print()

    print("=== Проверка методов ===")
    transport1.move()
    car1.move()
    car1.honk()
    bike1.move()
    print()

    print("=== Использование len() ===")
    print(f"Количество мест в {car1.brand}: {len(car1)}")
    print()


    print("=== Сравнение машин ===")
    print(f"car1 == car2: {car1 == car2}")
    print(f"car1 == car1: {car1 == car1}")
    print()

    print("=== Сложение скоростей ===")
    total_speed = car1 + car2
    print(f"Суммарная скорость car1 и car2: {total_speed} km/h")
    print()


    print("=== Попытка сложить машину и велосипед ===")
    try:
        result = car1 + bike1
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    # 5. Дополнительное задание
    print("=== Дополнительное задание ===")

    vehicles = [
        Transport("Generic", 60),
        Car("BMW", 150, 4),
        Car("Ford", 110, 5),
        Bike("Trek", 30, "road"),
        Bike("Specialized", 20, "mountain")
    ]


    for vehicle in vehicles:
        vehicle.move()