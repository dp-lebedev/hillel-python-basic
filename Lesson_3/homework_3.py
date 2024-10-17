# ДЗ 3.1
# ======
print("Вітаємо у додатку Simple calc!")
print()
print("Калькулятор працює наступним чином: користувач послідовно вводить два ЦІЛІ числа (a та b), а також знак математичної операції (+, -, *. /)\n"
      "Додаток бере перше введене число (a) та виконує над ним вказану дію з використанням другого числа (b).")
print()
number_a = int(input("Введіть перше число: "))
number_b = int(input("Введіть друге число: "))
math_sign = input("Введіть арифметичну дію (+, -, *, /): ")

# Для зменшення рядків коду можна використати виведення результату обчислень по закінченню роботи if-else. Якщо ж if-else достатньо великий - можна виводити результат безпосередньо всередині відповідного умовного оператора.
#Результат ділення перетворюємо на int, щоб виводилось ціле число, якщо ділення відбувається без залишку. Бо всі інші результати також мають тип даних int. В принципі, тут можна додати ще один if, який буде перевіряти залишок від ділення і, якщо він дорівнює 0, то виводити його з типом int, а якщо не дорівнює 0, - виводити, як float.

if math_sign == "+":
    math_res = number_a + number_b
    # print(math_res)
elif math_sign == "-":
    math_res = number_a - number_b
    # print(math_res)
elif math_sign =="*":
    math_res = number_a * number_b
    # print(math_res)
elif math_sign == "/":
    if number_b == 0:
        math_res = "ділення на 0 неприпустиме!"
    else:
        math_res = int(number_a / number_b)
        # print(math_res)
else:
    math_res = "було введено неприпустимий знак математичної дії!"
print("Результат обчислень:", math_res)

match math_sign:
    case "+":
        math_res = number_a + number_b
    case "-":
        math_res = number_a - number_b
    case "*":
        math_res = number_a * number_b
    case "/":
        if number_b == 0:
            math_res = "ділення на 0 неприпустиме!"
        else:
            math_res = int(number_a / number_b)
    case _:
        math_res = "було введено неприпустимий знак математичної дії!"
print("Результат обчислень:", math_res)

# ДЗ 3.2
# ======
numbers = [12, 3, 4, 10]
# numbers = [1]
# numbers = []
# numbers = [12, 3, 4, 10, 8]
if len(numbers) == 0:
    print("Список порожній, неможливо виконати переміщення елементу:", numbers)
elif len(numbers) == 1:
    print("Список містить лише один елемент, неможливо виконати переміщення елементу:", numbers)
else:
    print("Список до переміщення останнього елементу на першу позицію:", numbers)
    move_element = (numbers[-1])
    numbers.remove(move_element)
    numbers.insert(0, move_element)
    print("Список після переміщення останнього елементу на першу позицію:", numbers)

# ДЗ 3.3
# ======
divide_list = [1, 2, 3, 4, 5, 6]
# divide_list = [1, 2, 3]
# divide_list = [1, 2, 3, 4, 5]
# divide_list = [1]
# divide_list = []
if divide_list == []:
    list_part1 = []
    list_part2 = []
elif len(divide_list) == 1:
    list_part1 = divide_list
    list_part2 = []
elif len(divide_list) % 2 == 0:
    list_part1 = divide_list[: len(divide_list) // 2]
    list_part2 = divide_list[len(divide_list) // 2 :]
else:
    # Оскільки ціла частина від ділення непарного числа дорівнює порядковому номеру того елемента, який необхідно помістити в перший список (починаючи з елемента під номером 0) і при цьому цей елемент не входить до вибірки під час виконання зрізу колекеції - додаємо одиницю до необхідної кількості елементів в зрізі.
    part1_count = len(divide_list)//2 + 1
    list_part1 = (divide_list[:part1_count])
    list_part2 = (divide_list[part1_count:])
result = ([list_part1, list_part2])
print("Початковий список має вигляд:", divide_list)
print("Результат розділення початкового списку на два списки:", result)