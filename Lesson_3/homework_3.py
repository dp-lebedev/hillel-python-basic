# ДЗ 3.1
# ======
print("Вітаємо у додатку Simple calc!")
print()
print("Калькулятор працює наступним чином: користувач послідовно вводить два числа (a та b), а також знак математичної операції (+, -, *. /)\nДодаток бере перше введене число (a) та виконує над ним вказану дію з використанням другого числа (b).")
print()
number_a = int(input("Введіть перше число: "))
number_b = int(input("Введіть друге число: "))
math_sign = input("Введіть арифметичну дію (+, -, *, /): ")

# Для зменшення рядків коду можна використати виведення результату обчислень по закінченню роботи if-else. Якщо ж if-else достатньо великий - можна виводити результат безпосередньо всередині відповідного умовного оператора.
#Результат ділення перетворюємо на int, щоб виводилось ціле число, якщо ділення відбувається без залишку. В принципі, тут можна додати ще один if, який буде перевіряти залишок від ділення і, якщо він дорівнює 0, то виводити його з типом int, а якщо не дорівнює 0, - виводити, як float.

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
