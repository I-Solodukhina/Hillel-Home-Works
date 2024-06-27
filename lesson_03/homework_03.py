alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on'
                       ' where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it '
                       'doesn\'t matter which way you go," said the Cat.\n\"—— so long as I get somewhere," Alice '
                       'added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk '
                       'long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)
print("-" * 50)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800
sea_area_sum = black_sea_area + azov_sea_area
print(f'The total area of the Black and Azov Seas is {sea_area_sum} square kilometers')
print("-" * 50)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_items = 375_291
first_warehouse = all_items - 222_950
third_warehouse = all_items - 250_449
second_warehouse = all_items - first_warehouse - third_warehouse
print(f'First warehouse contains {first_warehouse} items. \nSecond warehouse contains {second_warehouse} items. '
      f'\nThird warehouse contains {third_warehouse} items.')
print("-" * 50)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_term = 18
monthly_payment = 1179
pc_cost = credit_term * monthly_payment
print(f'Total cost of the new PC is {pc_cost} UAH')
print("-" * 50)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f'The remainder of A = {a}, \nThe remainder of B = {b}, \nThe remainder of C = {c}, \nThe remainder of D = {d},'
      f' \nThe remainder of E = {e}, \nThe remainder of F = {f}')
print("-" * 50)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_size_pizza_price = 274
middle_size_pizza_price = 218
juice_price = 35
b_day_cake_price = 350
bottle_of_water = 21
order_total_cost = (big_size_pizza_price * 4) + (middle_size_pizza_price * 2) + (juice_price * 4) + b_day_cake_price + (
            bottle_of_water * 3)
print(f'Iryna\'s order total cost is: {order_total_cost} UAH')
print("-" * 50)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos_qty = 232
one_page_photo_capacity = 8
pages_in_album_total = all_photos_qty / one_page_photo_capacity
if all_photos_qty % one_page_photo_capacity == 0:
    print(f'Ihor will need {int(pages_in_album_total)} pages.')
else:
    print(f'Ihor will need {int(pages_in_album_total + 1)} pages.')
print("-" * 50)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
fuel_tank_capacity = 48
fuel_per_100_km = 9
total_fuel_needed = (total_distance / 100) * fuel_per_100_km
# refueling_count = total_fuel_needed / fuel_tank_capacity
print(f'Family will need {total_fuel_needed / fuel_tank_capacity} stops for the refueling and {total_fuel_needed} '
      f'liter of fuel.')
