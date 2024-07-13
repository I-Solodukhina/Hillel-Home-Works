'''
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це
зробити!”
Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
'''

array_to_operate = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3', 'RAV-4', '12, 23, 16', 'VFR 700', '11,1.2,22']


def sum_of_numbers_in_array(list_of_strings: list[str]):
    """
    Splits the list of strings into elements and calculates the sum of numbers in each strings if it can be converted
    to integers
    :param list_of_strings: list[str]
    """
    for strings in list_of_strings:
        try:
            split_string = strings.split(',')
            convert_strings_to_numbers = [int(numbers) for numbers in split_string]
            sum_received_numbers = sum(convert_strings_to_numbers)
            print(f"The sum of '{strings}' strings is: {sum_received_numbers}")
        except ValueError:
            print(f"Sorry, pal, I can't do this for '{strings}'")


sum_of_numbers_in_array(array_to_operate)
