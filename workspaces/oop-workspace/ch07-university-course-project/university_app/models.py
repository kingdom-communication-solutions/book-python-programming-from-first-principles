"""University Course System: model classes.

Starter file. Complete the classes so that check_university.py passes.
The project text in the book specifies every operation and its error messages.
"""

PASS_MARK = 50


class Course:
    def __init__(self, code, title, credits, capacity, prerequisites=()):
        self.code = code
        self.title = title
        self.credits = credits
        self.capacity = capacity
        self.prerequisites = tuple(prerequisites)
        # TODO: keep this course's enrollments


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.completed = {}  # course code -> grade of each passed course
        # TODO: keep this student's enrollments


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None


class University:
    def __init__(self, name, max_credits=30):
        self.name = name
        self.max_credits = max_credits
        # TODO: store courses and students by their IDs

    def add_course(self, course):
        raise NotImplementedError("add_course")

    def add_student(self, student):
        raise NotImplementedError("add_student")

    def courses(self):
        raise NotImplementedError("courses")

    def enroll(self, student_id, code):
        raise NotImplementedError("enroll")

    def record_grade(self, student_id, code, grade):
        raise NotImplementedError("record_grade")

    def enrolled_students(self, code):
        raise NotImplementedError("enrolled_students")

    def transcript(self, student_id):
        raise NotImplementedError("transcript")
