# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

set_range_to = 11
even_numbers = (num for num in range(set_range_to + 1) if num % 2 == 0)


for even_num in even_numbers:
    print(even_num)

print('-' * 50)


# ----------------------------------------------------------------------------------------------------------------------
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen_fib = fibonacci_generator()
range_fib = 7
for i in range(range_fib):
    print(next(gen_fib))
    input("Press Enter to continue...")
