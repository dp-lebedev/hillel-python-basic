# ДЗ 15.1
# =======
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        r3 = self.get_square() + other.get_square()
        return Rectangle(1,r3)

    def __mul__(self, n):
        r4 = self.get_square() * n
        return Rectangle(1, r4)

    def __str__(self):
        return f"Прямокутник({self.width}, {self.height})"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

# # ДЗ 15.2
# # =======
# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __float__(self):
#         if self.b == 0:
#             raise ZeroDivisionError()
#         return self.a / self.b
#
#     def __mul__(self, other):
#         f_d = Fraction(self.a * other.a, self.b * other.b)
#         return f_d
#
#     def __add__(self, other):
#         new_a = self.a * other.b + other.a * self.b
#         new_b = self.b * other.b
#         f_c = Fraction(new_a, new_b)
#         return f_c
#
#     def __sub__(self, other):
#         new_a = self.a * other.b - other.a * self.b
#         new_b = self.b * other.b
#         f_e = Fraction(new_a, new_b)
#         return f_e
#
#     def __eq__(self, other):
#         return self.a * other.b == self.b * other.a
#
#     def __gt__(self, other):
#         if isinstance(other, Fraction):
#             return self.__float__() > other.__float__()
#         else:
#             return False
#
#     def __lt__(self, other):
#         if isinstance(other, Fraction):
#            return self.__float__() < other.__float__()
#         else:
#             return False
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
#
# assert f_d < f_c  # True
# assert f_d > f_e  # True
# assert f_a != f_b  # True
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2  # True
# print('OK')