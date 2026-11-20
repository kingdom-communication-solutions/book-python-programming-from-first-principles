"""Acceptance checks for the University Course System project.

Run this file in the same folder as your models.py:

    python3 check_university.py      (macOS, Linux)
    py check_university.py           (Windows)

Each check prints PASS or FAIL with a short reason. The checks use only the
public interface described in the project text, and each one builds its own
small university, so one failing check does not affect the others. Extension
checks run only when the corresponding method exists. Do not change this
file; change your models.py until every check passes.
"""
from copy import deepcopy

from models import Course, Student, University


def build(max_credits=30):
    university = University("Riverside University", max_credits=max_credits)
    university.add_course(Course("C101", "Programming 1", 6, 2))
    university.add_course(Course("C102", "Mathematics 1", 6, 3))
    university.add_course(Course("C201", "Programming 2", 6, 2, ["C101"]))
    university.add_course(Course("C301", "Data Science Project", 12, 2, ["C201", "C102"]))
    students = {}
    for student_id, name in [("S1", "Ada"), ("S2", "Kofi"), ("S3", "Lena")]:
        students[student_id] = Student(student_id, name)
        university.add_student(students[student_id])
    return university, students


def observable_state(university, students, watched=()):
    """Copy public reports and retained objects, without inspecting private collections."""
    courses = university.courses()
    codes = [line.split()[0] for line in courses]
    return deepcopy((
        courses,
        [university.enrolled_students(code) for code in codes],
        [university.transcript(sid) for sid in students],
        [(s.student_id, s.name, s.completed) for s in students.values()],
        [(e.grade, e.student.student_id, e.student.name, e.student.completed,
          e.course.code, e.course.title, e.course.credits, e.course.capacity,
          e.course.prerequisites) for e in watched],
    ))


def expect_refusal(university, students, action, expected_message, watched=()):
    before = observable_state(university, students, watched)
    try:
        action()
    except ValueError as error:
        assert str(error) == expected_message, f"message was {str(error)!r}"
        after = observable_state(university, students, watched)
        assert after == before, "refusal changed observable state"
        return
    raise AssertionError("no ValueError was raised")


def enrolled_in_order():
    u, students = build()
    u.enroll("S1", "C101")
    u.enroll("S2", "C101")
    assert u.enrolled_students("C101") == ["Ada", "Kofi"], repr(u.enrolled_students("C101"))


def full_course():
    u, students = build()
    u.enroll("S1", "C101")
    u.enroll("S2", "C101")
    expect_refusal(u, students, lambda: u.enroll("S3", "C101"), "C101 is full")


def second_enrollment():
    u, students = build()
    u.enroll("S1", "C102")
    expect_refusal(u, students, lambda: u.enroll("S1", "C102"), "S1 is already enrolled in C102")


def missing_prerequisite():
    u, students = build()
    expect_refusal(u, students, lambda: u.enroll("S1", "C201"), "Missing prerequisite: C101")
    # The first missing prerequisite follows the course's list, not sorted order.
    expect_refusal(u, students, lambda: u.enroll("S1", "C301"), "Missing prerequisite: C201")
    u.enroll("S1", "C101")
    u.record_grade("S1", "C101", 50)
    u.enroll("S1", "C201")
    u.record_grade("S1", "C201", 50)
    expect_refusal(u, students, lambda: u.enroll("S1", "C301"), "Missing prerequisite: C102")


def unknown_ids():
    u, students = build()
    for _ in range(2):
        expect_refusal(u, students, lambda: u.enroll("S9", "C101"), "Unknown student: S9")
        expect_refusal(u, students, lambda: u.enroll("S1", "C999"), "Unknown course: C999")


def duplicate_course():
    u, students = build()
    enrollment = u.enroll("S1", "C101")
    u.record_grade("S1", "C101", 78)
    expect_refusal(u, students, lambda: u.add_course(Course("C101", "Copy", 99, 9)),
                   "Duplicate course code: C101", watched=(enrollment,))


def duplicate_student():
    u, students = build()
    enrollment = u.enroll("S1", "C101")
    u.record_grade("S1", "C101", 78)
    expect_refusal(u, students, lambda: u.add_student(Student("S1", "Replacement")),
                   "Duplicate student ID: S1", watched=(enrollment,))
    # The ID must still resolve to Ada with her passed prerequisite.
    assert u.enroll("S1", "C201").student is enrollment.student


def passed_prerequisite():
    u, students = build()
    u.enroll("S1", "C101")
    u.enroll("S2", "C101")
    u.record_grade("S1", "C101", 78)
    u.record_grade("S2", "C101", 45)
    assert u.enroll("S1", "C201") is not None, "enroll() should return the enrollment"
    expect_refusal(u, students, lambda: u.enroll("S2", "C201"), "Missing prerequisite: C101")


def grade_rules():
    u, students = build()
    enrollment = u.enroll("S1", "C102")
    # Test empty and already-recorded grades, including the completed dictionary.
    for existing in (None, 78):
        if existing is not None:
            u.record_grade("S1", "C102", existing)
        for invalid in (-1, 101, 75.5, "78", None, True):
            expect_refusal(u, students, lambda: u.record_grade("S1", "C102", invalid),
                           "Grade must be between 0 and 100", watched=(enrollment,))
    expect_refusal(u, students, lambda: u.record_grade("S3", "C102", 70),
                   "S3 is not enrolled in C102", watched=(enrollment,))


def grade_boundaries():
    u, students = build()
    enrollment = u.enroll("S1", "C102")
    for grade in (0, 49, 50, 100, 45):
        assert u.record_grade("S1", "C102", grade) is enrollment
        assert enrollment.grade == grade
        expected = {"C102": grade} if grade >= 50 else {}
        assert enrollment.student.completed == expected, enrollment.student.completed


def transcript():
    u, students = build()
    u.enroll("S1", "C101")
    u.enroll("S1", "C102")
    u.record_grade("S1", "C101", 78)
    u.enroll("S2", "C101")
    u.record_grade("S2", "C101", 45)
    assert u.transcript("S1") == ["C101 Programming 1: 78 (passed)", "C102 Mathematics 1: in progress"], \
        repr(u.transcript("S1"))
    assert u.transcript("S2") == ["C101 Programming 1: 45 (failed)"], repr(u.transcript("S2"))


def professor_grading():
    from models import Professor
    u, students = build()
    u.add_professor(Professor("P1", "Dr. Mensah"), teaches=["C101", "C201"])
    u.enroll("S1", "C101")
    enrollment = u.enroll("S3", "C102")
    assert u.record_grade("S1", "C101", 81, professor_id="P1") is not None
    expect_refusal(u, students, lambda: u.record_grade("S3", "C102", 60, professor_id="P1"), "P1 does not teach C102", watched=(enrollment,))


def credit_limit():
    u = University("Small College", max_credits=12)
    for code, title in [("C101", "Programming 1"), ("C102", "Mathematics 1"), ("C103", "Research Ethics")]:
        u.add_course(Course(code, title, 6, 3))
    students = {"S1": Student("S1", "Ada")}
    u.add_student(students["S1"])
    u.enroll("S1", "C101")
    u.enroll("S1", "C102")
    expect_refusal(u, students, lambda: u.enroll("S1", "C103"), "Credit limit of 12 exceeded")
    before = observable_state(u, students)
    assert u.recommend("S1") == [], repr(u.recommend("S1"))
    assert observable_state(u, students) == before, "recommend() changed state"
    u.record_grade("S1", "C101", 45)
    assert u.recommend("S1") == ["C103"], "graded courses must release credit load"
    u.enroll("S1", "C103")


def recommendations():
    u, students = build()
    u.enroll("S1", "C101")
    u.enroll("S2", "C101")
    before = observable_state(u, students)
    assert u.recommend("S3") == ["C102"], repr(u.recommend("S3"))
    assert observable_state(u, students) == before, "recommend() changed state"
    u.record_grade("S1", "C101", 50)
    assert u.recommend("S1") == ["C102", "C201"]
    limited, limited_students = build(max_credits=6)
    limited.enroll("S1", "C102")
    expect_refusal(limited, limited_students, lambda: limited.enroll("S1", "C201"),
                   "Missing prerequisite: C101")


CORE = [
    ("enrolled students are listed in order", enrolled_in_order),
    ("a full course is refused; refusals preserve state", full_course),
    ("a second enrollment is refused; refusals preserve state", second_enrollment),
    ("a missing prerequisite is refused; refusals preserve state", missing_prerequisite),
    ("unknown students and courses are refused; refusals preserve state", unknown_ids),
    ("a duplicate course code is refused without changing state", duplicate_course),
    ("a duplicate student ID is refused without changing state", duplicate_student),
    ("only a passed course satisfies a prerequisite; refusals preserve state", passed_prerequisite),
    ("invalid grades and grading a non-enrolled student preserve state", grade_rules),
    ("grade boundaries update the enrollment and passed-course record", grade_boundaries),
    ("the transcript lists every enrollment", transcript),
]
EXTENSION_A = [("extension A: supplied professor must teach the course; refusal preserves state", professor_grading)]
EXTENSION_B = [("extension B: credit-limit refusal preserves state", credit_limit),
               ("extension B: recommendations respect capacity and prerequisites", recommendations)]

checks = list(CORE)
if hasattr(University, "add_professor"):
    checks += EXTENSION_A
else:
    print("SKIP extension A: University.add_professor() not found")
if hasattr(University, "recommend"):
    checks += EXTENSION_B
else:
    print("SKIP extension B: University.recommend() not found")

passed = 0
for name, test in checks:
    try:
        test()
    except Exception as error:
        print(f"FAIL {name}  ({type(error).__name__}: {error})")
    else:
        print(f"PASS {name}")
        passed += 1
print(f"{passed} of {len(checks)} checks passed")

# A failing acceptance run must also fail in automated verification.
raise SystemExit(0 if passed == len(checks) else 1)
