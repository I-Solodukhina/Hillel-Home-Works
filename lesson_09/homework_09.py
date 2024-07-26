start_list = [104, 18.6, 'abc', 'xyz', 19, 199.4, 43.2, True, 78, 47, 64.12, 83, 443, 'the end']


def to_find_the_arithmetic_average(numbers: list) -> float:
    """
    Calculates the arithmetic mean of a list of numbers
    :param numbers: list
    :return: float
    """
    numbers_to_operate = [element for element in numbers if isinstance(element, (int, float))]
    return sum(numbers_to_operate) / len(numbers_to_operate)


# print(to_find_the_arithmetic_average(start_list))
# print('-' * 50)

# ----------------------------------------------------------------------------------------------------------------------
list_of_words_to_operate = ['Написати', 'функцію', 'яка', 'приймає', 'список', 'слів', 'та', 'повертає', 'найдовше',
                            'слово', 'у', 'списку']


def to_find_the_longest_word(some_word_list: list[str]) -> str:
    """
    Accepts a list of words and returns the longest word.
    :param some_word_list: list[str]
    :return: str
    """
    longest_word = max(some_word_list, key=len)
    return longest_word


# print(to_find_the_longest_word(list_of_words_to_operate))
# print('-' * 50)

# ----------------------------------------------------------------------------------------------------------------------

def count_capitalized_words(text):
    all_words = text.split()
    capitalized_words = [word for word in all_words if word.istitle()]
    return len(capitalized_words)


text_to_operate = ('Росте та й росте той син, як з води,— не багато літ, а вже великий виріс. Одного разу батько з '
                   'сином копали колодязь,— докопались до великого каменя. Батько побіг кликати людей, щоб допомогли '
                   'його викинути. Поки батько ходив, а Котигорошко узяв та й викинув. Приходять люде, як глянули — аж '
                   'поторопіли, так злякались, що в його така сила, та й хотіли його вбити. А він підкинув того каменя '
                   'вгору та й підхопив,— люде й повтікали.')

# print(count_capitalized_words(text_to_operate))

# ----------------------------------------------------------------------------------------------------------------------
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


# print(to_find_the_even_nums(list_we_need_for_the_hw))
# print('-' * 50)

# ----------------------------------------------------------------------------------------------------------------------

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
# print(f'You will need {total_pages_counter(all_photos_qty, one_page_photo_capacity)} pages')
