# ДЗ 10.1
# -------
def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

    yield begin
    current_value = begin
    for _ in range(1, end):
        current_value = func(current_value)
        yield current_value

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')


# # ДЗ 10.2
# # -------
# from string import ascii_letters, punctuation, digits
# def first_word(text):
#     """ Пошук першого слова """
#     text_clear = ""
#     for letter in text:
#         # Через те, що у нас є останній рядок, в якому відсутній пробіл, а замість нього присутня крапка -
#         # змінюємо всі знаки пунктуації, окрім апострофу, на пробіли.
#         # *Додатково перевіряємо на присутність цифр і міняємо їх на пробіли, якщо вони є.
#         if letter in digits or letter in punctuation and letter !="'":
#             letter = " "
#         text_clear += letter
#     # Формуємо з очищеного рядка колекцію зі словами і виводимо перший елемент такої колекції.
#     words_in_string = text_clear.split()
#     return words_in_string[0]
#
# print(first_word("3 Hello 567 world"))
# print(first_word("greetings, friends"))
# print(first_word("don't touch it"))
# print(first_word(".., and so on ..."))
# print(first_word("hi"))
# print(first_word("Hello.World"))
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

# # ДЗ 10.3
# # -------
# def is_even(digit):
#     """ Перевірка чи є парним число """
#     # Перевіряємо, чи дорівнює залишок від ділення нулю. Якщо так - число є парним.
#     if digit % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(2))
# print(is_even(5))
# print(is_even(0))
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

