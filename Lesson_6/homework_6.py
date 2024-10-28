# # ДЗ 6.1
# # ------
#
# import string
#
# # Запит на введення букв з діапазону.
# print("Виведення букв в діапазоні, який ввів користувач.")
# print()
# first_letter = input("Введіть початкову букву з діапазону: ")
# last_letter = input("Введіть останню букву з діапазону: ")
#
# # Визначаємо індекси введених букв.
# first_letter_index = string.ascii_letters.index((first_letter))
# last_letter_index = string.ascii_letters.index(last_letter)
#
# # print("Букви: ", first_letter, " - ", last_letter)
# # print("Індекси: ", first_letter_index, " ~ ", last_letter_index)
#
# # Щоб включити до виводу на екран більшу з введених букв - додаємо +1 до другого елементу зрізу.
# if first_letter_index < last_letter_index:
#     print(string.ascii_letters[first_letter_index:last_letter_index + 1])
# elif first_letter_index > last_letter_index:
#     print(string.ascii_letters[last_letter_index:first_letter_index + 1])
# else:
#     print(first_letter)
#
# # Код по якому є запитання, бо відпрацьовує не кожного разу.
# # print("Букви: ", first_letter, " - ", last_letter)
# # print("Індекси: ", first_letter_index, " ~ ", last_letter_index)
# #
# # if first_letter < last_letter:
# #     print(string.ascii_letters[first_letter_index:last_letter_index + 1])
# # elif first_letter > last_letter:
# #     print(string.ascii_letters[last_letter_index:first_letter_index + 1])
# # else:
# #     print(first_letter)

# # ДЗ 6.2
# # ------
#
# print("Перетворення числа, яке ввів користувач на дні, години, хвилини та секунди.")
# print()
#
# DAYS_1_ETC = [1, 21, 31, 41, 51, 61, 71, 81, 91]
# DAYS_2_ETC = [2, 22, 32, 42, 52, 62, 72, 82, 92]
# DAYS_3_ETC = [3, 4, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 93, 94]
#
# HOURS_1_ETC = [1, 21]
# HOURS_2_ETC = [2, 3, 4, 22, 23]
#
# MINS_SECS_1_ETC = [1, 21, 31, 41, 51]
# MINS_SECS_2_ETC = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]
#
# user_try = "y"
#
# while user_try == "y":
#     user_input_number = int(input("Введіть число в діапазоні від 0 до 8640000 (вісім мільйонів шістсот сорок тисяч): "))
#     if 0 <= user_input_number <= 8640000:
#         # Залишок секунд від введеного числа та число хвилин.
#         user_input_mins, user_input_secs = divmod(user_input_number, 60)
#         # print("Minutes:", user_input_mins)
#         # print("Seconds:", user_input_secs)
#
#         # Залишок хвилин та число годин.
#         user_input_hours, user_input_mins = divmod(user_input_mins, 60)
#         # print("Hours:", user_input_hours)
#         # print("Minutes:", user_input_mins)
#
#         # Залишок годин та число діб.
#         user_input_days, user_input_hours = divmod(user_input_hours, 24)
#         # print("Days:", user_input_days)
#         # print("Hours:", user_input_hours)
#
#         # Формуємо коректний вигляд тексту з урахуванням відмінків та числа (однина/множина).
#         # Дні.
#         # if user_input_days in (1, 21, 31, 41, 51, 61, 71, 81, 91):
#         if user_input_days in DAYS_1_ETC:
#             days_text = "день"
#         # elif user_input_days in (2, 22, 32, 42, 52, 62, 72, 82, 92):
#         elif user_input_days in DAYS_2_ETC:
#             days_text = "дня"
#         # elif user_input_days in (3, 4, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 93, 94):
#         elif user_input_days in DAYS_3_ETC:
#             days_text = "дні"
#         else:
#             days_text = "днів"
#
#         # Години.
#         # if user_input_hours in (1, 21):
#         if user_input_hours in HOURS_1_ETC:
#             hours_text = "година"
#         # elif user_input_hours in (2, 3, 4, 22, 23):
#         elif user_input_hours in HOURS_2_ETC:
#             hours_text = "години"
#         else:
#             hours_text = "годин"
#
#         # Хвилини.
#         # if user_input_mins in (1, 21, 31, 41, 51):
#         if user_input_mins in MINS_SECS_1_ETC:
#             mins_text = "хвилина"
#         # elif user_input_mins in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54):
#         elif user_input_mins in MINS_SECS_2_ETC:
#             mins_text = "хвилини"
#         else:
#             mins_text = "хвилин"
#
#         # Секунди
#         # if user_input_secs in (1, 21, 31, 41, 51):
#         if user_input_secs in MINS_SECS_1_ETC:
#             secs_text = "секунда"
#         # elif user_input_secs in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54):
#         elif user_input_secs in MINS_SECS_2_ETC:
#             secs_text = "секунди"
#         else:
#             secs_text = "секунд"
#
#         # Приводимо години, хвилини та секунди до двозначного числа, якщо їхнє значення менше 10.
#         if int(user_input_hours) < 10:
#             user_input_hours = str(user_input_hours).zfill(2)
#         if int(user_input_mins) < 10:
#             user_input_mins = str(user_input_mins).zfill(2)
#         if int(user_input_secs) < 10:
#             user_input_secs = str(user_input_secs).zfill(2)
#
#         print(f"Ви ввели число: {user_input_number}.")
#         print()
#         print(
#             f"Результат перетворення Вашого числа на кількість днів, годин, хвилин та секунд: {user_input_days} {days_text}, {user_input_hours} {hours_text}, {user_input_mins} {mins_text}, {user_input_secs} {secs_text}.")
#         break
#     else:
#         print("Введено число з діапазону, який не є дозволеним.")
#         user_try = input("Повторити спробу? Натисніть \"y\", для повторної спроби, будь яку іншу клавішу для виходу з програми. ")

# ДЗ 6.3
# ------

print("Розібрати число, яке ввів користувач на цифри, з яких воно складається, та множити їх, доки результат не буде меншим або таким, що дорівнює дев'яти.")

