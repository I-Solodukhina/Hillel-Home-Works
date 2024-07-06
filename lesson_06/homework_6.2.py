# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    word_with_h = input('Enter the word, that contains letter "h" (uppercase or lowercase): ')
    if 'h' in word_with_h.lower():
        print('You did it!')
        break
    else:
        print('Try again')
