# ДЗ 5.1
# ------
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import keyword
import string

print("Запит на введення імені змінної.")
print("Змінна не може:\n- починатися з цифри;\n- містити великі літери;\n- містити пробіл та знаки пунктуації, окрім нижнього підкреслення;\n- бути жодним із зареєстрованих слів;\n- повне ім'я змінної повинно містити не більше одного нижнього підкреслення.")
print()
user_input_string = str(input("Введіть назву змінної: "))
print("Ви ввели:", user_input_string)

if user_input_string[0] in string.digits:
    check_result = "False digits"
elif user_input_string in keyword.kwlist:
   check_result = "False keyword"
elif user_input_string.count("_") > 1:
    check_result = "False underscore count"
else:
    for char in user_input_string:
        if char.isupper():
            check_result = "False uppercase"
            break
        elif char in string.whitespace:
            check_result = "False space"
            break
        elif char in string.punctuation and char != "_":
            check_result = "False punctuation"
            break
        else:
            check_result = "True string"
print(check_result)

# # ДЗ 5.2
# # ______
# print("Вітаємо у додатку Simple calc!")
# print()
# print("Калькулятор працює наступним чином: користувач послідовно вводить два ЦІЛІ числа (a та b), а також знак математичної операції (+, -, *. /)\n"
#       "Додаток бере перше введене число (a) та виконує над ним вказану дію з використанням другого числа (b).")
# print()
#
# continue_calc = "y"
#
# while continue_calc == "y":
#     number_a = int(input("Введіть перше число: "))
#     number_b = int(input("Введіть друге число: "))
#     math_sign = input("Введіть арифметичну дію (+, -, *, /): ")
#
#     match math_sign:
#         case "+":
#             math_res = number_a + number_b
#         case "-":
#             math_res = number_a - number_b
#         case "*":
#             math_res = number_a * number_b
#         case "/":
#             if number_b == 0:
#                 math_res = "ділення на 0 неприпустиме!"
#             else:
#                 math_res = int(number_a / number_b)
#         case _:
#             math_res = "було введено неприпустимий знак математичної дії!"
#     print("Результат обчислень:", math_res)
#     print()
#     continue_calc = input("Бажаєте виконати ще одне обчислення?\nВведіть \"y\", якщо так. Введіть будь-який інший символ для завершення роботи. ")
#
# print("Роботу калькулятора завершено.")

# # ДЗ 5.3
# # ______
# import string
#
# input_string = input("Введіть рядок для перетворення його на hashtag (#): ")
# print("Ви ввели рядок:", input_string)
#
# # Для запобігання використання великих літер в середині слова, спочатку робимо всі букви маленькими.
# input_string = input_string.lower()
#
# # Робимо перші букви кожного слова великими.
# input_string = input_string.title()
#
# # Прибираємо символи пунктуації та пробіли.
# input_string_clean = ""
# for char in input_string:
#     if char not in string.punctuation and char not in string.whitespace:
#         input_string_clean += char
# print("Рядок з великою першою буквою кожного слова, без символів пунктуації та пробілів:", input_string_clean)
#
# # Визначаємо максимальний індекс в рядку.
# input_string_max_index = len(input_string_clean) - 1
#
# # За потреби - обрізаємо рядок до 139 символів. Бо 140 символом буде знак hashtag.
# if input_string_max_index >= 139:
#     input_string_139 = input_string_clean[0:139]
# else:
#     input_string_139 = input_string_clean
#
# # Додаємо символ # та формуємо остаточний вигляд hashtag-у.
# hashtag_string = "#" + input_string_139
# print(hashtag_string)
