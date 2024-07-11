# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number: int):
    """
    Друкує результати множення на задане число лише до максимального значення для добутку - 25
    :param number: int
    """
    multiplier = 1  # Initialize the appropriate variable
    while True:   # Complete the while loop condition.
        result = number * multiplier
        if result > 25:
            break  # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1  # Increment the appropriate variable


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print(('-' * 50) + 'task 1')

# ------------------------------------------------------------------------------------------------------------task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def adding_numbers(number_1: int | float, number_2: int | float) -> int:
    """
    Calculates the sum of two numbers
    :param number_1: first number
    :param number_2: second number
    :return: int
    """
    result = number_1 + number_2
    return result


print(adding_numbers(800, 13598))

print(('-' * 50) + 'task 2')

# ------------------------------------------------------------------------------------------------------------task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

start_list = [104, 18.6, 'abc', 'xyz', 19, 199.4, 43.2, True, 78, 47, 64.12, 83, 443, 'the end']


def to_find_the_arithmetic_average(numbers: list) -> float:
    """
    Calculates the arithmetic mean of a list of numbers
    :param numbers: list
    :return: float
    """
    numbers_to_operate = [element for element in numbers if isinstance(element, (int, float))]
    return sum(numbers_to_operate) / len(numbers_to_operate)


print(to_find_the_arithmetic_average(start_list))

print(('-' * 50) + 'task 3')

# ------------------------------------------------------------------------------------------------------------task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

string_to_operate = 'Написати функцію, яка приймає рядок та повертає його у зворотному порядку'


def to_reverse_the_string(some_string: str) -> str:
    """
    Accepts a string and returns it in reverse order.
    :param some_string: string
    :return: str: in reverse order
    """
    return some_string[::-1]


print(to_reverse_the_string(string_to_operate))

print(('-' * 50) + 'task 4')

# ------------------------------------------------------------------------------------------------------------task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

word_list_to_operate = ['Написати', 'функцію', 'яка', 'приймає', 'список', 'слів', 'та', 'повертає', 'найдовше',
                        'слово', 'у', 'списку']


def to_find_the_longest_word(some_word_list: list[str]) -> str:
    """
    Accepts a list of words and returns the longest word.
    :param some_word_list: list[str]
    :return: str
    """
    longest_word = max(some_word_list, key=len)
    return longest_word


print(to_find_the_longest_word(word_list_to_operate))

print(('-' * 50) + 'task 5')

# ------------------------------------------------------------------------------------------------------------task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1: str, str_2: str) -> int:
    """
    Accepts two strings and returns the index of the first occurrence of the second string in the first string if the
    second string is a substring of the first string, and -1 if the second string is not a substring of the first string.
    :param str_1: str: first string
    :param str_2: str: second string
    :return: int: index
    """
    return str_1.find(str_2)


str1 = "Hello, world!"
str2 = ","
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cow"
print(find_substring(str1, str2))

print(('-' * 50) + 'task 6')

# ------------------------------------------------------------------------------------------------------------task 7
"""  Завдання 7-10: Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


def if_text_is_longer_than_n() -> bool:
    """
    Counts the number of unique characters of the string and return the result of comparing this number with the
    specified value (10)
    :return: bool
    """
    text_we_need = set(
        input('Complete the sentence: "If you\'re happy and you know it " - '))
    if len(text_we_need) > 10:
        return True
    else:
        return False


print(if_text_is_longer_than_n())

print(('-' * 50) + 'task 7')

# ------------------------------------------------------------------------------------------------------------task 8
#Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і
# маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


def we_need_the_letter_h():
    """
    Requires the user to enter a word with the letter 'h'
    """
    while True:
        h_word = input('Enter the word, that contains letter "h" (uppercase or lowercase): ')
        if 'h' in h_word.lower():
            print('You did it!')
            break
        else:
            print('Try again')


we_need_the_letter_h()

print(('-' * 50) + 'task 8')

# ------------------------------------------------------------------------------------------------------------task 9
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_we_need_for_the_hw = [104, 18, 19, 199, 43, 78, 47, 64, 83, 443, 1212]


def to_find_the_even_nums(even_num_list: list[int]) -> int:
    """
    Accepts a list of numbers, calculates the sum of all even numbers in this list.
    :param even_num_list: list[int]: list of numbers
    :return: int: sum of all even numbers
    """
    the_even_numbers = []
    for element in even_num_list:
        if element % 2 == 0:
            the_even_numbers.append(element)
    return sum(the_even_numbers)


print(to_find_the_even_nums(list_we_need_for_the_hw))

print(('-' * 50) + 'task 9')

# ------------------------------------------------------------------------------------------------------------task 10
# Ігор займається фотографією. Він вирішив зібрати всі свої 232 фотографії та вклеїти в альбом. На одній сторінці може
# бути розміщено щонайбільше 8 фото. Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото?


def total_pages_counter(all_items_count: int, one_page_cap: int) -> int:
    """
    Calculates how many whole pages should the album have.
    :param all_items_count: int: total count of the photos
    :param one_page_cap: int: max count of photos that can be placed on the whole one page.
    :return: int
    """
    pages_in_album_total = all_items_count / one_page_cap
    if all_items_count % one_page_cap == 0:
        return int(pages_in_album_total)
    else:
        return int(pages_in_album_total + 1)


all_photos_qty = 232
one_page_photo_capacity = 8
print(f'You will need {total_pages_counter(all_photos_qty, one_page_photo_capacity)} pages')

print(('-' * 50) + 'task 10')
