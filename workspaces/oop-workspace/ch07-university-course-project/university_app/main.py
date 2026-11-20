"""Start the University Course System with sample data. Course listing works after Milestone 3; full commands require Milestone 5."""
from controller import OfficeController
from models import Course, Student, University
from views import ConsoleView


def build_university():
    university = University("Riverside University", max_credits=30)
    university.add_course(Course("C101", "Programming 1", 6, 2))
    university.add_course(Course("C102", "Mathematics 1", 6, 3))
    university.add_course(Course("C201", "Programming 2", 6, 2, ["C101"]))
    university.add_course(Course("C301", "Data Science Project", 12, 2, ["C201", "C102"]))
    for student_id, name in [("S1", "Ada"), ("S2", "Kofi"), ("S3", "Lena")]:
        university.add_student(Student(student_id, name))
    return university


def main():
    OfficeController(build_university(), ConsoleView()).run()


if __name__ == "__main__":
    main()
