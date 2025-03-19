"""
Create objects based on the previous home task
"""

class Student:
    """
    Represents a student with attributes like ID, name, and total marks.
    """

    def __init__(self, student_id: int, first_name: str, last_name: str, total_mark: int):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.total_mark = total_mark

    def update_info(self, **kwargs):
        """Update student information dynamically."""
        for key, value in kwargs.items():
            setattr(self, key, value)

class StudentAnswer:
    """
    Contains student_id and the boolean answer (True, False) indicating attendance.
    """

    def __init__(self, student_id: int, answer: bool):
        self.student_id = student_id
        self.answer = answer

class Party:
    """
    Manages the list of invited students and operations:
     1. Invite Student
     2. Remove Student
     3. Notify Student is not invited
     4. Get invited students
     5. Get total Price
    """

    COSTS_PER_PERSON = {
        "juice": 2,
        "salad": 3.5,
        "main_dish": 20.25,
        "dessert": 8
    }
    SNACK_COST = 6
    DISCOUNT_THRESHOLD = 8
    DISCOUNT_RATE = 0.15

    def __init__(self):
        self.invited_students = []

    def invite_student(self, student: Student):
        """Adds a student to the invitation list if they meet the criteria."""
        if student.total_mark >= 250:
            self.invited_students.append(student)
        else:
            self.notify_student_not_invited(student)

    def remove_student(self, student_id: int):
        """Removes a student from the invitation list."""
        self.invited_students = [s for s in self.invited_students if s.student_id != student_id]

    def notify_student_not_invited(self, student: Student):
        """Prints a message if a student is not invited due to low marks."""
        print(f"Student {student.first_name} {student.last_name} is not invited due to low marks.")

    def get_invited_students(self):
        """Returns a list of invited students."""
        return self.invited_students

    def get_total_price(self):
        """Calculates the total cost of the party based on attendees."""
        total_attendees = len(self.invited_students)
        base_price = sum(self.COSTS_PER_PERSON.values()) * total_attendees
        snack_cost = (total_attendees // 4) * self.SNACK_COST

        total_price = base_price + snack_cost
        if total_attendees > self.DISCOUNT_THRESHOLD:
            total_price *= (1 - self.DISCOUNT_RATE)

        print(f"Number of people attending: {total_attendees}, Total Price: ${total_price:.2f}")
        return total_price


   
