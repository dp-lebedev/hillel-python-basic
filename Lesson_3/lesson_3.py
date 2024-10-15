# n1, n2 = 10, 20 # множинне привласнення
# print(n1 == n2) # поверне True, якщо обидва операнди однакові
# print(n1 != n2) # поверне True, якщо обидва операнди різні
# print(1 ==1 and 3 ==3) # поверне True, якщо обидва операнди рівні
# print(1 ==1 or 3 ==3) # поверне True, якщо хоча б один операнд дорівнює True
#
# is_valid = False
# print(not is_valid) # not - інверсія. Якщо було True - стане False. Виключно для типу даних boolean.
#
# print("hello" in "hello world") # in - вміст елемента в колекції.

# hours = int(input("Enter hours: "))
# v1
# if hours >= 12:
#     print("PM")
# else:
#     print("AM")

# v2
# if 12 <= hours < 24: # або hours >= 12 and hours < 24. Перший синтаксис можна використовувати, якщо є проміжки.
#     print("PM")
# elif 0 <= hours < 12:
#     print("AM")
# else:
#     print("incorrect hours")

# film_rating = int(input("Enter film rating: "))
#
# if 0 < film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("Film OK")
#     else:
#         print("Film not OK")
# else:
#     print("Incorrect rating")

# Для роботи з однією змінною та константами можна використовувати match
# match user_select:
#     case 1:
#         print("1")
#     case 2:
#         print("2")
#     case _:
#         print("Incorrect input")

# Тернарний оператор
number_b = 3
number_a = 10 if number_b < 5 else 20 # Значить таке: якщо number_b < 5, то number_a = 10, інакше number_a = 20. Можна записати це ж простим if-else.

# Перше ДЗ зробити двома способами. Через IF-ELSE та через MATCH.