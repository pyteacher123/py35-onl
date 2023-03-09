class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.great = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be str.")

        self._name = value


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_best_students(self):
        answer = []
        for student in self.students:
            great_set = set(student.great)
            bad_marks_set = set(1, 2, 3, 4, 7, 8, 9, 10)
            result = bad_marks_set.intersection(great_set)
            if not result:
                answer.append(student)
        return answer
