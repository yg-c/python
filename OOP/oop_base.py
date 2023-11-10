# OOP base
class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name: str, max_students: int):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student: Student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student(name='Tim', age=19, grade=95)
s2 = Student(name='Bill', age=19, grade=75)
s3 = Student(name='Jill', age=19, grade=65)

course = Course(name='Science', max_students=2)

course.add_students(s1)
course.add_students(s2)

print(course.get_average_grade())
