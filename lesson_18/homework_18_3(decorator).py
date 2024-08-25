import functools


# Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


@log_function_call
def to_find_the_longest_word(some_word_list: list[str]) -> str:
    """
    Accepts a list of words and returns the longest word.
    :param some_word_list: list[str]
    :return: str
    """
    longest_word = max(some_word_list, key=len)
    return longest_word


@log_function_call
def count_capitalized_words(text):
    all_words = text.split()
    capitalized_words = [word for word in all_words if word.istitle()]
    return len(capitalized_words)


@log_function_call
def to_find_the_arithmetic_average(numbers: list) -> float:
    """
    Calculates the arithmetic mean of a list of numbers
    :param numbers: list
    :return: float
    """
    numbers_to_operate = [element for element in numbers if isinstance(element, (int, float))]
    return sum(numbers_to_operate) / len(numbers_to_operate)


list_to_operate = [104, 18.6, 'abc', 'xyz', 19, 199.4, 43.2, True, 78, 47, 64.12, 83, 443, 'the end']
list_of_words_to_operate = ['Написати', 'функцію', 'яка', 'приймає', 'список', 'слів', 'та', 'повертає', 'найдовше',
                            'слово', 'у', 'списку']

text_to_operate = ('Росте та й росте той син, як з води,— не багато літ, а вже великий виріс. Одного разу батько з '
                   'сином копали колодязь,— докопались до великого каменя. Батько побіг кликати людей, щоб допомогли '
                   'його викинути. Поки батько ходив, а Котигорошко узяв та й викинув. Приходять люде, як глянули — аж '
                   'поторопіли, так злякались, що в його така сила, та й хотіли його вбити. А він підкинув того каменя '
                   'вгору та й підхопив,— люде й повтікали.')

to_find_the_arithmetic_average(list_to_operate)
to_find_the_longest_word(list_of_words_to_operate)
count_capitalized_words(text_to_operate)

print('-' * 50)

# ----------------------------------------------------------------------------------------------------------------------
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An Exception occurred in '{func.__name__}': {e}")
            return None
    return wrapper


@exception_handler
def sum_of_numbers_in_array(list_of_strings: list[str]):
    """
    Splits the list of strings into elements and calculates the sum of numbers in each strings if it can be converted
    to integers
    :param list_of_strings: list[str]
    """
    for strings in list_of_strings:
        split_string = strings.split(',')
        convert_strings_to_numbers = [int(numbers) for numbers in split_string]
        sum_received_numbers = sum(convert_strings_to_numbers)
        print(f"The sum of '{strings}' strings is: {sum_received_numbers}")


array_to_operate = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3', 'RAV-4', '12, 23, 16', 'VFR 700', '11,1.2,22']
sum_of_numbers_in_array(array_to_operate)
