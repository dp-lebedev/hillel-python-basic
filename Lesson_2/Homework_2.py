#### ДЗ 2.1
input_number = int(input ("Enter four-digit number: "))
input_digit_4 = input_number % 10
input_digit_3 = (input_number % 100 - input_digit_4) / 10
input_digit_2 = (input_number % 1000 - input_digit_3*10 - input_digit_4) /100
input_digit_1 = input_number // 1000

# Перетворення на int зроблено, оскільки для input_digit_2 та input_digit_3 тип поля з результатом обчислень був float.
# Для input_digit_1 та input_digit_4 це було зроблено для того, щоб код був уніфікованим для всієї програми.
print("Ви ввели число:", input_number)
print()
print("Цифра в розряді тисяч:", int(input_digit_1))
print()
print("Цифра в розряді сотень:", int(input_digit_2))
print()
print("Цифра в розряді десятків:", int(input_digit_3))
print()
print("Цифра в розряді одиниць:", int(input_digit_4))