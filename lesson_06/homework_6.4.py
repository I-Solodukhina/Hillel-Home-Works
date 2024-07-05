list_we_need_for_the_hw = [104, 18, 19, 199, 43, 78, 47, 64, 83, 443]

# 1.

the_even_numbers = []

for element in list_we_need_for_the_hw:
    if element % 2 == 0:
        the_even_numbers.append(element)

print(sum(the_even_numbers))

# 2.

print(sum(elem for elem in list_we_need_for_the_hw if elem % 2 == 0))
