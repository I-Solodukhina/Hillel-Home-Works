# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    # def __init__(self, __side_length):
    #     self.__side_length = __side_length
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14 * self.__radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.__radius


circle = Circle(5)
print(circle.get_area())
print(circle.get_perimeter())


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def get_area(self):
        return self.__side_length ** 2

    def get_perimeter(self):
        return 4 * self.__side_length


square = Square(5)
print(square.get_area())
print(square.get_perimeter())


class Triangle(Figure):
    def __init__(self, side_length_1, side_length_2, side_length_3):
        self.__side_length_1 = side_length_1
        self.__side_length_2 = side_length_2
        self.__side_length_3 = side_length_3

    def get_area(self):
        p = (self.__side_length_1 + self.__side_length_2 + self.__side_length_3) / 2
        return (p * (p - self.__side_length_1) * (p - self.__side_length_2) * (p - self.__side_length_3)) ** 0.5

    def get_perimeter(self):
        return self.__side_length_1 + self.__side_length_2 + self.__side_length_3


triangle = Triangle(3, 4, 5)
print(triangle.get_area())
print(triangle.get_perimeter())
