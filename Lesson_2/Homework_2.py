#### ДЗ 2.1
input_4number = input ("Введіть чотиризначне число: ")
# Перетворення на int окремою змінною необхідно для коректного відображення введеного числа, якщо перші декілька
# введених символів - то нули (наприклад, 0057).
input_4number_int = int(input_4number)
input_digit_4 = input_4number_int % 10
input_digit_3 = (input_4number_int % 100 - input_digit_4) / 10
input_digit_2 = (input_4number_int % 1000 - input_digit_3*10 - input_digit_4) /100
input_digit_1 = input_4number_int // 1000

# Перетворення на int зроблено, оскільки для input_digit_2 та input_digit_3 тип поля з результатом обчислень був float.
# Для input_digit_1 та input_digit_4 це було зроблено для того, щоб код був уніфікованим для всієї програми.
print("Ви ввели число:", input_4number)
print()
print("Цифра в розряді тисяч:", int(input_digit_1))
print()
print("Цифра в розряді сотень:", int(input_digit_2))
print()
print("Цифра в розряді десятків:", int(input_digit_3))
print()
print("Цифра в розряді одиниць:", int(input_digit_4))


#### ДЗ 2.2
input_5number = input("Введіть п'ятизначне число: ")
# Перетворення на int окремою змінною необхідно для коректного відображення введеного числа, якщо перші декілька
# введених символів - то нули (наприклад, 00578).
input_5number_int = int(input_5number)
input_digit_1 = input_5number_int // 10000
input_digit_2 = input_5number_int // 1000 - input_digit_1 * 10
input_digit_3 = input_5number_int // 100 - input_digit_2 * 10 - input_digit_1 * 100
input_digit_4 = input_5number_int // 10 - input_digit_3 * 10 - input_digit_2 * 100 - input_digit_1 * 1000
input_digit_5 = input_5number_int % 10
# Збираємо число з введених цифр у дзеркальному відображенні
input_5number_mirrored = input_digit_5 * 10000 + input_digit_4 * 1000 + input_digit_3 * 100 + input_digit_2 * 10 + input_digit_1

print("Ви ввели число:", input_5number)
print()
print("Ваше число у дзеркальному відображенні:", input_5number_mirrored)