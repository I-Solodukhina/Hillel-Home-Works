import unittest
from lesson_09.homework_09 import to_find_the_arithmetic_average
from lesson_09.homework_09 import to_find_the_longest_word
from lesson_09.homework_09 import total_pages_counter
from lesson_09.homework_09 import to_find_the_even_nums
from lesson_09.homework_09 import count_capitalized_words


class TheArithmeticAverage(unittest.TestCase):
    # Функція, що тестується, повертає середнє арифметичне значення для елементів типу int або float зі списку

    def test_negative_if_list_contains_only_strings(self):
        # Перевіряємо, що список тільки з елементами типу str викличе ZeroDivisionError

        data = ['abc', 'xyz', 'the end']
        with self.assertRaises(ZeroDivisionError):
            result = to_find_the_arithmetic_average(data)

    def test_if_local_list_contains_only_ints_or_floats(self):
        # Перевіряємо, що функція оперує тільки елементами з типом int та float

        result = to_find_the_arithmetic_average(
            [104, 18.6, 'abc', 'xyz', 19, 199.4, 43.2, True, 78, 47, 64.12, 83, 443, 'the end'])
        self.assertTrue(result, isinstance(int, float))

    def test_negative_if_argument_contains_not_iterable_obj(self):
        # Перевіряємо, що неітеруємий об'єкт в аргументі функції викличе помилку типу даних

        data = 555
        with self.assertRaises(TypeError):
            result = to_find_the_arithmetic_average(data)


# ----------------------------------------------------------------------------------------------------------------------
class TheLongestWord(unittest.TestCase):
    # Функція, що тестується, приймає список слів та повертає найдовше

    def test_if_word_is_longest(self):
        # Перевіряємо чи в результаті маємо найдовше слово

        input_words = ['Canada', 'USA', 'Ukraine', 'France', 'Peru', 'Brazil', 'Poland',
                       'UAE', 'Chili', 'Qatar', 'Japan', 'Thailand', 'Malaysia', 'Denmark']
        expected_result = 'Thailand'
        result = to_find_the_longest_word(input_words)
        self.assertEqual(result, expected_result)

    def test_negative_if_list_elements_is_not_str(self):
        # Перевіряємо, що список з елементами не тільки типу str викличе помилку TypeError

        input_words = ['Canada', 125, 'Ukraine', 'France', 'Peru', 'Brazil', 'Poland', True, 12.5, {},
                       'UAE', 'Chili', 'Qatar', 'Japan', 'Thailand', 'Malaysia', 'Denmark']
        with self.assertRaises(TypeError):
            result = to_find_the_longest_word(input_words)


# ----------------------------------------------------------------------------------------------------------------------
class TotalPagesCounter(unittest.TestCase):
    # Функція, що тестується, вираховує необхідну кількість цілих сторінок фотоальбому, виходячи з кількості фотографій

    def test_if_pages_qty_is_int(self):
        # Перевіряємо, чи завжди функція повертає ціле число (кількість цілих сторінок)

        result = total_pages_counter(111, 8)
        self.assertTrue(result, int)

    def test_negative_if_arguments_contains_not_int_type(self):
        # Перевіряємо, що інший тип даних в аргументах функції викличе помилку типу даних

        with self.assertRaises(TypeError):
            result = total_pages_counter(111, '8')


# ----------------------------------------------------------------------------------------------------------------------
class TheEvenNumbers(unittest.TestCase):
    # Функція, що тестується, вираховує суму тільки парних цілих чисел списку з числами

    def test_if_numbers_to_operate_are_even(self):
        # Перевіряємо, що функція оперує коректно з елементами типу int, float

        result = to_find_the_even_nums(
            [104, 18, 19, 199, 43.0, 78.5, 47, 64, 83, 12.0, 1212])
        self.assertTrue(result, isinstance(result, int | float))

    def test_negative_if_argument_list_contains_not_int_type(self):
        # Перевіряємо, що інший тип даних в аргументах функції викличе помилку типу даних

        with self.assertRaises(TypeError):
            result = to_find_the_even_nums([104, 18, 19, '199', 43.0, 78.5, 47, 64, 83, 12.0, '1212'])


# ----------------------------------------------------------------------------------------------------------------------
class CapitalizedWordsCounter(unittest.TestCase):
    # Функція, що тестується, вираховує кількість слів, які починаються з великої літери

    def test_if_capitalized_words_qty_is_correct(self):
        # Перевіряємо, що функція повертає правильну кількість слів

        result = count_capitalized_words(
            'Росте та й росте той син, як з води,— не багато літ, а вже великий виріс. Одного разу батько з '
            'сином копали колодязь,— докопались до великого каменя. Батько побіг кликати людей, щоб допомогли '
            'його викинути. Поки батько ходив, а Котигорошко узяв та й викинув. Приходять люде, як глянули — аж '
            'поторопіли, так злякались, що в його така сила, та й хотіли його вбити. А він підкинув того каменя '
            'вгору та й підхопив,— люде й повтікали.'
        )
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
