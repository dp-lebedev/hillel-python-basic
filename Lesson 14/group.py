from group_limit_error import GroupLimitError

class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = []
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group)  == self.student_limit:
            raise GroupLimitError("У групі вже є 10 студентів. Немає місця для нових.")
        self.group.append(student)

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
        separator = "=" * 10
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Група: {self.number}\n{separator}\nСтуденти:\n{all_students} '