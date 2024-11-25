# # ДЗ 14.1
# # =======
# class GroupLimitError(Exception):
#     def __init__(self, message):
#         self.message = message
#
# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f'ПІБ: {self.first_name} {self.last_name}.\nСтать: {self.gender}. Вік (років): {self.age}'
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return super().__str__() + f'. Запис в книзі: {self.record_book}\n----'
#
# class Group:
#
#     def __init__(self, number, student_limit=10):
#         self.number = number
#         self.group = []
#         self.student_limit = student_limit
#
#     def add_student(self, student):
#         if len(self.group)  == self.student_limit:
#             raise GroupLimitError("У групі вже є 10 студентів. Немає місця для нових.")
#         self.group.append(student)
#
#     def delete_student(self, last_name):
#         for student in self.group.copy():
#             if student.last_name == last_name:
#                 self.group.remove(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#
#     def __str__(self):
#         all_students = ''
#         separator = "=" * 10
#         for student in self.group:
#             all_students += student.__str__() + '\n'
#         return f'Група: {self.number}\n{separator}\nСтуденти:\n{all_students} '
#
# st1 = Student('Чоловіча', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Жіноча', 25, 'Liza', 'Taylor', 'AN145')
# st3 = Student('Чоловіча', 30, 'John', 'Snow', 'AN146')
# st4 = Student('Жіноча', 30, 'Daenerys', 'Targaryen', 'AN147')
# st5 = Student('Чоловіча', 30, 'Khal', 'Drogo', 'AN148')
# st6 = Student('Жіноча', 30, 'Sersei', 'Lannister', 'AN149')
# st7 = Student('Чоловіча', 30, 'Joffrey', 'Baratheon', 'AN150')
# st8 = Student('Жіноча', 30, 'Sansa', 'Stark', 'AN151')
# st9 = Student('Чоловіча', 30, 'Ramsay', 'Bolton', 'AN152')
# st10 = Student('Жіноча', 30, 'Ygritte', 'Wild', 'AN153')
# st11 = Student('Чоловіча', 30, 'Gregor', 'Clegane', 'AN154')
# gr = Group('PD1')
# try:
#     gr.add_student(st1)
#     gr.add_student(st2)
#     gr.add_student(st3)
#     gr.add_student(st4)
#     gr.add_student(st5)
#     gr.add_student(st6)
#     gr.add_student(st7)
#     gr.add_student(st8)
#     gr.add_student(st9)
#     gr.add_student(st10)
#     gr.add_student(st11)
#
# except GroupLimitError as error:
#     print(error)
#
# print(gr)
#
# # print(str(gr.find_student('Jobs')))
# # print(gr.find_student('Jobs2'))
# # print(isinstance(gr.find_student('Jobs'), Student))
#
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!

# ДЗ 14.2
# =======
from student import Student
from group_limit_error import GroupLimitError
from group import Group

st1 = Student('Чоловіча', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Жіноча', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Чоловіча', 30, 'John', 'Snow', 'AN146')
st4 = Student('Жіноча', 30, 'Daenerys', 'Targaryen', 'AN147')
st5 = Student('Чоловіча', 30, 'Khal', 'Drogo', 'AN148')
st6 = Student('Жіноча', 30, 'Sersei', 'Lannister', 'AN149')
st7 = Student('Чоловіча', 30, 'Joffrey', 'Baratheon', 'AN150')
st8 = Student('Жіноча', 30, 'Sansa', 'Stark', 'AN151')
st9 = Student('Чоловіча', 30, 'Ramsay', 'Bolton', 'AN152')
st10 = Student('Жіноча', 30, 'Ygritte', 'Wild', 'AN153')
st11 = Student('Чоловіча', 30, 'Gregor', 'Clegane', 'AN154')
gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)

except GroupLimitError as error:
    print(error)

print(gr)

# print(str(gr.find_student('Jobs')))
# print(gr.find_student('Jobs2'))
# print(isinstance(gr.find_student('Jobs'), Student))

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
