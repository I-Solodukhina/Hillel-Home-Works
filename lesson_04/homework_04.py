adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawyer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")
print(adventures_of_tom_sawyer)
print('-' * 50)

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace('....', ' ')
print(adventures_of_tom_sawyer)
print('-' * 50)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawyer = ' '.join(adventures_of_tom_sawyer.split())
print(adventures_of_tom_sawyer)
print('-' * 50)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f'There are {adventures_of_tom_sawyer.count("h")} letters \'h\' in the text')
print('-' * 50)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""


def count_capitalized_words(text):
    all_words = text.split()
    capitalized_words = [word for word in all_words if word.istitle()]
    return len(capitalized_words)


print(f'The text contains {count_capitalized_words(adventures_of_tom_sawyer)} capitalized words')
print('-' * 50)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom = adventures_of_tom_sawyer.find('Tom')
second_tom = adventures_of_tom_sawyer.find('Tom', first_tom + 1)
print(f'The word \'Tom\' is found on the {second_tom} position')
print('-' * 50)

# task 07
""" Розділіть змінну adventures_of_tom_sawyer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawyer_sentences
"""
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split('. ')
print(adventures_of_tom_sawyer_sentences)
print('-' * 50)

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawyer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adventures_of_tom_sawyer_sentences[3].lower())
print('-' * 50)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for element in adventures_of_tom_sawyer_sentences:
    if element.startswith("By the time"):
        print('Yes one of the sentences starts with the "By the time" text')

print('-' * 50)

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawyer_sentences.
"""
words_from_the_last_sentence = adventures_of_tom_sawyer_sentences[-1].split(' ')

print(f"The last sentence contains {len(words_from_the_last_sentence)} words")
print('-' * 50)
