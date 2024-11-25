# # ДЗ 13.1
# # =======
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'ПІБ: {self.first_name} {self.last_name}. Стать: {self.gender}. Вік (років): {self.age}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f'. Запис в книзі: {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Група: {self.number}\nСтуденти:\n{all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
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

# # ДЗ 13.2
# # =======
# class Counter:
#
#    def __init__(self, current=1, min_value=0, max_value=10):
#        self.current = current
#        self.min_value = min_value
#        self.max_value = max_value
#
#    def set_current(self, start):
#        if start > self.max_value:
#            raise ValueError("Досягнуто максимальне значення.")
#        elif start < self.min_value:
#            raise ValueError("Досягнуто мінімальне значення.")
#        self.current = start
#
#    def set_max(self, max_max):
#         self.max_value = max_max
#
#    def set_min(self, min_min):
#        self.min_value = min_min
#
#    def step_up(self):
#        if self.current + 1 > self.max_value:
#            raise ValueError("Досягнуто максимум.")
#        self.set_current(self.current + 1)
#
#    def step_down(self):
#        if self.current -1 < self.min_value:
#            raise ValueError("Досгнуто мінімум.")
#        self.set_current(self.current - 1)
#
#    def get_current(self):
#        return self.current
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# print("Test1 - ", counter.get_current())
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e) # Достигнут максимум
# print("Test2 - ", counter.get_current())
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# print("Test3 - ", counter.get_current())
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e) # Достигнут минимум
# print("Test4 - ", counter.get_current())
# assert counter.get_current() == 7, 'Test4'