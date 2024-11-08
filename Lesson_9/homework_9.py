# ДЗ 9.1
# ------
def popular_words (text, words):
    # Перетворюємо поданий рядок на рядок лише з маленькими літерами та створюємо з нього список.
    text_lower = text.lower().split()
    dict_for_text = {}
    for word in words:
        dict_for_text[word] = text_lower.count(word)
    return dict_for_text


print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# # ДЗ 9.2
# # ------
#
# def difference(*numbers):
#     if not numbers:
#         num_min = 0
#         num_max = 0
#     else:
#         num_min = min(numbers)
#         num_max = max(numbers)
#     num_diff = num_max - num_min
#     if type(num_diff) == float:
#         num_diff = round(num_diff, 2)
#     return num_diff
#
# print(difference(1, 2, 3))
# print(difference(5, -5))
# print(difference(10.2, -2.2, 0, 1.1, 0.5))
# print(difference())
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')

# # v. 2
# # ----
# from decimal import Decimal
#
# def difference(*numbers):
#     if not numbers:
#         num_min = 0
#         num_max = 0
#     else:
#         numbers = [Decimal(str(num)) for num in numbers]
#         num_min = min(numbers)
#         num_max = max(numbers)
#     num_diff = num_max - num_min
#     if type(num_diff) == Decimal:
#         num_diff = float(num_diff)
#     return num_diff
#
# print(difference(1, 2, 3))
# print(difference(5, -5))
# print(difference(10.2, -2.2, 0, 1.1, 0.5))
# print(difference())
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')