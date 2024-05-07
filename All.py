class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def counting_grades(self):
        lst_grades = self.grades['Python']
        amount_lst = sum(lst_grades)
        average_rating = amount_lst / len(lst_grades)
        average = round(average_rating, 1)
        return average

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
                       f'{student_best.counting_grades()}\n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
                       f'{" ".join(self.finished_courses)}'
        return some_student
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def calculation_grades(self):
        values = self.course_grades['Python']
        sum_lst = sum(values)
        midle_grade = sum_lst / len(values)
        return midle_grade

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{cool_lecturer.calculation_grades()}\n'
        return self.some_lecturer

    def __str1__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{cool_lecturer_1.calculation_grades()}'
        return self.some_lecturer

    def __eq__(self):
        return (cool_lecturer.calculation_grades() == cool_lecturer_1.calculation_grades())

    def __ge__(self):
        return (cool_lecturer.calculation_grades() >= cool_lecturer_1.calculation_grades())

    def __lt__(self):
        return (cool_lecturer.calculation_grades() < cool_lecturer_1.calculation_grades())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviever = f'Имя: {self.name}\nФамилия: {self.surname}'
        return self.some_reviever
 
student_best_1 = Student('Михаил', 'Светлоземельцев', 'Famale')
student_best_1.courses_in_progress += ['Python', 'Git']
student_best_1.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Семен', 'Видящий')
cool_lecturer.courses_attached += ['Python']

student_best_1.rate(cool_lecturer, 'Python', 10)
student_best_1.rate(cool_lecturer, 'Python', 8)
student_best_1.rate(cool_lecturer, 'Python', 9)

student_best = Student('Юрий', 'Вислоухов', 'Famale')
student_best.courses_in_progress += ['Python']
student_best.finished_courses += ['Введение в программирование']

cool_lecturer_1 = Lecturer('Алексей', 'Щербинский')
cool_lecturer_1.courses_attached += ['Python']

student_best.rate(cool_lecturer_1, 'Python', 10)
student_best.rate(cool_lecturer_1, 'Python', 8)
student_best.rate(cool_lecturer_1, 'Python', 9)

some_reviewer = Reviewer('Николай', 'Апрельский')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(student_best, 'Python', 7)
some_reviewer.rate_hw(student_best, 'Python', 9)
some_reviewer.rate_hw(student_best, 'Python', 10)

def mid_grades_lecturer(lecturers, course):
    counter = 0
    len_grades = 0
    lecturers = [cool_lecturer, cool_lecturer_1]
    course = ['Python' , ]
    for cors in course:
        for lecturer in lecturers:
            counter += sum(lecturer.__dict__['course_grades'][cors])
            len_grades += len(lecturer.__dict__['course_grades'][cors])
    return f"Средняя оценка за курс {cors} у всех лекторов {counter / len_grades}"
print (mid_grades_lecturer(cool_lecturer, 'Python'), '\n')

def mid_grades_student(students, course):
    counter = 0
    len_grades = 0
    students = [student_best, ]
    course = ['Python' , ]
    for cors in course:
        for student in students:
            counter += sum(student.__dict__['grades'][cors])
            len_grades += len(student.__dict__['grades'][cors])
    return f"Средняя оценка за курс {cors} у всех студентов {round(counter / len_grades, 1)}"
print (mid_grades_student(student_best, 'Python'), '\n')
print('Student:') 
print(student_best.grades, '\n')

print('Lecturer:')
print(cool_lecturer.course_grades, '\n')
print('Student:')
print(student_best.__str__(), '\n')

print('Lecturer:')
print(cool_lecturer.__str__())
print(cool_lecturer_1.__str1__(), '\n')

print('Reviewer:')
print(some_reviewer.__str__(), '\n')

print('Равные средние оценки лекторов:')
print(cool_lecturer.__eq__() == cool_lecturer_1.__eq__(), '\n')

print('Средняя оценка первого лектора больше или равна средней оценки второго:')
print(cool_lecturer.__ge__() >= cool_lecturer_1.__ge__(), '\n')

print('Средняя оценка первого лектора меньше средней оценки второго:')
print(cool_lecturer.__lt__() < cool_lecturer_1.__lt__(), '\n')
