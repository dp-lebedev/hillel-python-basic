# # ДЗ 8.1
# # ------
# def add_one(some_list):
#     # Створюємо змінну, в яку послідовно записуємо елементи списку.
#     string_temp = ""
#     for i in some_list:
#         string_temp += str(i)
#     # Перетворюємо рядок на число і додаємо до нього одиницю.
#     string_temp = int(string_temp) + 1
#     # Виконуємо зворотнє перетворення числа на список.
#     new_list = []
#     for char in str(string_temp):
#         new_list.append(int(char))
#     # print(new_list)
#     return(new_list)
#
# print(add_one([1, 2, 3, 4]))
# print(add_one([9, 9, 9]))
# print(add_one([0]))
# print(add_one([9]))
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

# # ДЗ 8.2
# # ------
# def is_palindrome(text):
#     import string
#     text_clear = ""
#     for char in text:
#         # Перевіряємо, чи є в переданому рядку цифри і, якщо є, виводимо False.
#         if char in string.digits:
#             return(False)
#         # Видаляємо з поданого рядка знаки пунктуації та пробіли.
#         elif char not in string.punctuation and char not in string.whitespace:
#             text_clear += char
#             text_clear = text_clear.lower()
#     # Перевіряємо, чи є рядок паліндромом.
#     # Створюємо нову змінну, до якої вносимо заданий рядок в зворотньому порядку.
#     text_backward = text_clear[::-1]
#     # print(text_backward)
#     # Перевіримо, чи є два рядки (поданий та звернений) однаковими.
#     if text_clear == text_backward:
#         return(True)
#     else:
#         return(False)
#
# print(is_palindrome('A man, a plan, a canal: Panama'))
# print(is_palindrome('0P'))
# print(is_palindrome('a.'))
# print(is_palindrome('aurora'))
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

# # ДЗ 8.3
# # ======
# def find_unique_value(some_list):
#     # Послідовно з першого числа перевіряємо, чи зустрічається воно лише один раз в списку.
#     # Якщо так - виводимо його.
#     for list_number in some_list:
#         if some_list.count(list_number) == 1:
#             return list_number
#
# print(find_unique_value([1, 2, 1, 1]))
# print(find_unique_value([2, 3, 3, 3, 5, 5]))
# print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")