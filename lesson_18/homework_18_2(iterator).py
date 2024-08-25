# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


list_to_reverse = [1, 2, 11, 'Ase Ventura', 77, 8.8, 50, 4, 165.5, 9, True]
reverse_list = ReverseListIterator(list_to_reverse)

for num in reverse_list:
    print(num)

# list_to_reverse = [1, 2, 11, 'Ase Ventura', 77, 8.8, 50, 4, 165.5, 9, True]
# reversed_list = iter(reversed(list_to_reverse))
# print(next(reversed_list))
# try:
#     print(next(reversed_list))
# except StopIteration:
#     print("StopIteration")

print('-' * 50)

# ----------------------------------------------------------------------------------------------------------------------
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.


class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration


in_range = 13
even_iterator = EvenNumbersIterator(in_range)

for number in even_iterator:
    print(number)
