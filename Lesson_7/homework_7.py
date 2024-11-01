# # ДЗ 7.1
# # ------
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

# Запит на перший набір, що складається з імені та віку.
user_name = input("Введіть 'Alex': ")
user_age = input("Введіть '32':")
# Викликаємо функцію і одразу в print виводимо результат її роботи.
print(say_hi(user_name, user_age))
assert say_hi(user_name, user_age) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
print()

# Запит на другий набір, що складається з імені та віку.
user_name = input("Введіть 'Frank': ")
user_age = input("Введіть '68':")
# Викликаємо функцію і результат її роботи записуємо в змінну, яку потім використовуємо для виводу результату.
return_from_def = say_hi(user_name, user_age)
print(return_from_def)
assert say_hi(user_name, user_age) == "Hi. My name is Frank and I'm 68 years old", 'Test2'

# # ДЗ 7.2
# # ------
# import string
# def correct_sentence(text):
#     if text[0] not in string.ascii_uppercase:
#         text = text.capitalize()
#     if text[-1] != ".":
#         text = text + "."
#     # # Як виправити, якщо рядок має вигляд "Greetings, Friends"?
#     # string_len = len(text)
#     # i = 0
#     # text_new = ""
#     # for i in string_len:
#     #     if text[i] in text.capitalize and text[i-1] == string.whitespace and text[i-2] == ",":
#     #         text[i] = text.lower()
#     #     text_new = text[i]
#     #     i += 1
#     return f"{text}"
#
# print(correct_sentence("greetings, friends"))
# print(correct_sentence("hello"))
# print(correct_sentence("Greetings. Friends"))
# print(correct_sentence("Greetings, friends."))
# print(correct_sentence("greetings, friends."))
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

# # ДЗ 7.3
# # ------
# def second_index(text, some_str):
#     # Шукаємо перше входження.
#     first_index = text.find(some_str)
#     # Сповіщення, якщо жодного входження немає.
#     if first_index == -1:
#         return None
#     # Шукаємо друге входження.
#     second_index = text.find(some_str, first_index + 1)
#     # Якщо другого входження немає.
#     if second_index == -1:
#         return None
#     # Якщо знайшли друге входження.
#     else:
#         return second_index
#
# print(second_index("sims", "s"))
# print(second_index("find the river", "e"))
# print(second_index("hi", "h"))
# print(second_index("Hello, hello", "lo"))
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

# # ДЗ 7.4
# # ------
#
# def common_elements():
#     # Отримуємо список елементів, що діляться на 3.
#     divided_by_3 = set()
#     for i3 in range(100):
#         if i3 % 3 == 0:
#             divided_by_3.add(i3)
#     # Отримуємо список елементів, що діляться на 5.
#     divided_by_5 = set()
#     for i5 in range(100):
#         if i5 % 5 ==0:
#             divided_by_5.add(i5)
#     # Порівнюєм два списки і виводимо лише спільні елементи.
#     common_elements = divided_by_3 & divided_by_5
#
#     return common_elements
#
#
# print(common_elements())
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}