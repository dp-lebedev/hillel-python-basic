# # ДЗ 12.1
# # -------

import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        result = []
        for text_string in file:
            text_in_line = re.findall(r">(.+)</", text_string)
            result += text_in_line
        print(f"Result: {result}")
    with open(result_file, 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write('\n'.join(result))

delete_html_tags("draft.html")

# # ДЗ 12.2
# # -------
# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"Товар: {self.name}, вартість: {self.price} грн."
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}, телефон: {self.numberphone}"
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         all_products = ""
#         for product, count in self.products.items():
#             all_products += f"\n{product.name}: {count} шт."
#         return f"Покупець: {self.user}\nПокупки:{all_products}"
#
#     def get_total(self):
#         all_sum = 0
#         for product, count in self.products.items():
#             all_sum += (product.price * count)
#         return all_sum
#
# lemon = Item('lemon', 5, "yellow", "small", )
# apple = Item('apple', 2, "red", "middle", )
# print(lemon)  # lemon, price: 5
#
# buyer = User("Ivan", "Ivanov", "02628162")
# print(buyer)  # Ivan Ivanov
#
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
#
# assert cart.get_total() == 40