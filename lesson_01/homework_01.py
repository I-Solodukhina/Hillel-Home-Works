# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")
print("-" * 50)

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")
print("-" * 50)

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)
print("-" * 50)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apple_trees = 2
banana = apple_trees * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)
print("-" * 50)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?

"""
apple_trees = 4
pears_trees = apple_trees + 5
plums_trees = apple_trees - 2
print(apple_trees + pears_trees + plums_trees)
print("-" * 50)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?

"""
morning_temperature = 5
afternoon_temperature = morning_temperature - 10
evening_temperature = afternoon_temperature + 4
print(evening_temperature)
print("-" * 50)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?

"""
boys = 24
girls = int(boys / 2)
print(boys - 1 + girls - 2)
print("-" * 50)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

"""
book_one_price = 8
book_two_price = book_one_price + 2
book_three_price = (book_one_price + book_two_price) / 2
print(book_one_price + book_two_price + book_three_price)
print("-" * 50)
