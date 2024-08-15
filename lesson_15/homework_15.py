# Створіть клас геометричної фігури "Пералелограм". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a)
# сторона_б (довжина сторони b)
# кут_1 (кут між сторонами a і b)
# кут_2 (кут між сторонами b і a)
# Необхідно реалізувати наступні вимоги:
#
# Значення сторін повинні бути більше 0.
# Сума кутів повинна дорівнювати 360 градусів.
# Для встановлення значень атрибутів використовуйте метод setattr.

class Parallelogram:
    def __init__(self, side_a, side_b, angle_1, angle_2):
        self.side_a = side_a
        self.side_b = side_b
        self.angle_1 = angle_1
        self.angle_2 = angle_2
        self.check_angles_summ()

    def __setattr__(self, key, value):
        if key in ('side_a', 'side_b',) and value <= 0:
            raise ValueError('Value must be > 0')
        elif key in ('angle_1', 'angle_2') and (0 <= value >= 180):
            raise ValueError('Value must be < 180')
        else:
            self.__dict__[key] = value

    def check_angles_summ(self):
        if self.angle_1 + self.angle_2 != 180:
            raise ValueError('Angles sum must be 180')

    def __str__(self):
        return f'Parallelogram: side_a = {self.side_a}, side_b = {self.side_b}, angle_1 = {self.angle_1}, angle_2 = {self.angle_2}'


figure = Parallelogram(side_a=10, side_b=20, angle_1=50, angle_2=50)
print(figure)
