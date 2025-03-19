COURSE_GRADE_MAX = 500
students = [
    {
        "student_id": 1,
        "first_name": "Arthur",
        "last_name": "Pendragon",
        "total_mark": 420,
    },
    {"student_id": 2, "first_name": "Guinevere", "last_name": None, "total_mark": 301},
    {"student_id": 3, "first_name": "Morgan", "last_name": "le Fay", "total_mark": 520},
    {
        "student_id": 4,
        "first_name": "Lancelot",
        "last_name": "du Lac",
        "total_mark": 140,
    },
    {
        "student_id": 5,
        "first_name": "Merlin",
        "last_name": "Hernandez",
        "total_mark": 500,
    },
]

def generate_student_id() -> int:
    max_student_id = max(student["student_id"] for student in students)
    return max_student_id + 1

def create_student(first_name: str, last_name: str, total_mark: int) -> dict:
    new_student = {
        "student_id": generate_student_id(),
        "first_name": first_name,
        "last_name": last_name,
        "total_mark": total_mark,
    }
    students.append(new_student)
    return new_student

def remove_student_by_id(student_id: int) -> bool:
    global students
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            return True
    raise Exception(f"Student with id {student_id} is missing")

def update_student(student_id: int, **kwargs) -> bool:
    for student in students:
        if student["student_id"] == student_id:
            for key, value in kwargs.items():
                if key != "student_id":
                    student[key] = value
            return True
    raise Exception(f"Student with id {student_id} not found")

def is_student_invited(student: dict) -> bool:
    return student["total_mark"] >= 250

def notify_student_failed_course(student: dict) -> None:
    print(f"Student {student['first_name']} {student['last_name']} has failed the course.")

def get_invited_students(students: list, invitation_rating_grade: int = 250) -> list:
    invited_students = []
    for student in students:
        if is_student_invited(student):
            invited_students.append(student)
        else:
            notify_student_failed_course(student)
    return invited_students

