# ДЗ 11.1
# -------
def prime_generator(end):
    # Створюємо функцію, яка буде визначати, чи є число простим.
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Формуємо список з простих чисел з використанням функції is_prime.
    for num in range(2, end + 1):
        if is_prime(num):
            yield num


from inspect import isgenerator

print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

# # ДЗ 11.2
# # -------
# def generate_cube_numbers(end):
#     # Визначаємо перше число, яке будемо підносити до куба, створюємо порожній список для обчислених значень.
#     number_to_cube = 2
#     cubes_list = []
#     while True:
#         # Обчислюємо куб числа, доки значення кубу не буде більшим за необхідне (end)
#         cube_value = number_to_cube ** 3
#         if cube_value > end:
#             break
#         cubes_list.append(cube_value)
#         yield cube_value
#         number_to_cube += 1
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# generate_cube_numbers(10)
# generate_cube_numbers(100)
# list(generate_cube_numbers(1000))
#
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

# # ДЗ 11.3
# # -------
# def is_even(number):
#     """ Перевірка чи є парним число """
#     # Перетворюємо число на рядок, створюємо шаблон для парних чисел та перевіряємо, чи присутній останній елемент отриманого числа в шаблоні.
#     number_as_string = str(number)
#     pair_pattern = str([0,2,4,6,8])
#     if number_as_string[-1] in pair_pattern:
#         return True
#     else:
#         return False
#
# print(is_even(2494563894038**2))
# print(is_even(1056897**2))
# print(is_even(24945638940387**3))
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'