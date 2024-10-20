# # ДЗ 4.1
# # ======
#
# # Окремо не опрацьовуються випадки, коли список складається лише з одного елементу, який є нулем.
# # Також не проводиться перевірка на наявність будь-якої кількості нулів, що розміщені з кінця списку.
# # Зроблено це виключно заради універсальності коду. Бо він коректно відпрацьовує і для списків без нулів.
# list_1 = [0, 1, 0, 12, 3]
# # list_1 = [0]
# # list_1 = [1, 0, 13, 0, 0, 0, 5]
# # list_1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# print("Початковий список:", list_1)
#
# # Визначаємо кількість елементів в списку і додаємо це значення в змінну для подальшого використання.
# # Щоб перейти від кількості елементів в списку до індексів - зменшуємо отримане значення на 1.
# list_1_max_index = len(list_1) - 1
#
# i = 0
#
# # Шукаємо нулі в списку і додаємо їхню кількість в змінну null_count.
# null_count = 0
# while i <= list_1_max_index:
#     if list_1[i] == 0:
#         null_count += 1
#     i += 1
#
# print("Кількість нулів в списку:", null_count)
#
# null_move = 1
# while null_move <= null_count:
#     list_1.remove(0)
#     list_1.append(0)
#     null_move += 1
#
# print("Змінений список:", list_1)

# # ДЗ 4.2
# # ======
#
# list_2 = [0, 1, 7, 2, 4, 8]
# # list_2 = [1, 3, 5]
# # list_2 = [6]
# # list_2 = []
#
# # # Визначаємо кількість елементів в списку і додаємо це значення в змінну для подальшого використання.
# list_2_len = len(list_2)
#
# print("Кількість елементів в списку:", list_2_len)
#
# # Припиняємо роботу програми, якщо кількість елементів в списку дорівнює нулю.
# while list_2_len == 0:
#     print("Значення останнього індексу визначити неможливо.")
#     print("Зупинено подальше виконання коду програми.")
#     break
#
# # Знаходимо парні індекси та виконуємо дії над ними.
# if list_2_len >0:
#     number_counter = 0
#     print("Початкове значення змінної, до якої будуть додаватись значення парного індексу:", number_counter)
#     for i in range(list_2_len):
#         if i % 2 == 0:
#             number_counter += list_2[i]
#             print("Поточне значення змінної", number_counter)
#     list_multiplier = list_2[-1]
#     print("Значення множника:", list_multiplier)
#
#     list_2_result = number_counter * list_multiplier
#     print("Фінальне значення (сума значень парних індексів помножена на значення останнього елементу індексу):", list_2_result)

# ДЗ 4.3
# ======
import random

# Випадково обираємо кількість елементів в списку
random_list_count = random.randint(3, 10)
print("Кількість елементів в списку, що буде створено:", random_list_count, "\n")

# Створюємо порожній список і додаємо в нього кількість елементів, визначену змінною random_list_count.
# Кожен елемент, що додається має значення від 0 до 9.
random_list = []
for i in range (random_list_count):
    random_list.append(random.randint(0, 9))
print("Список елементів створеного списку:", random_list, "\n")

# Зі створеного списку в окремі змінні заносимо значення першого, третього та другого з кінця елементу.
random_list_member_p0 = random_list[0]
random_list_member_p2 = random_list[2]
random_list_member_m2 = random_list[-2]
print("Перший, третій та другій з кінця елемент створеного списку:")
print(random_list_member_p0, random_list_member_p2, random_list_member_m2, sep=', ')
print()

# Створюємо власний список, до якого додаємо обрані вище три елементи.
my_random_list = []
my_random_list.append(random_list_member_p0)
my_random_list.append(random_list_member_p2)
my_random_list.append(random_list_member_m2)

print("Власний список:", my_random_list)
