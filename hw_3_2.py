import logging
from random import choice
from math import ceil
from hw_3_1 import invited_students_list


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def generate_students_answers(invited_students_list: list) -> tuple:
    """
    Simulates whether each invited student will attend the party.
    
    Args:
        invited_students_list (list): List of invited students.
    
    Returns:
        tuple: A tuple of (student_id, answer) where answer is True (attending) or False (not attending).
    """
    answer_list = (True, False)
    return tuple((student["student_id"], choice(answer_list)) for student in invited_students_list)


def print_total_price(invited_students: list) -> None:
    """
    Calculates and logs the total cost of the party based on attending students.

    Args:
        invited_students (list): List of invited students.
    
    Logs:
        Total number of attendees and total price.
    """
    students_answers = generate_students_answers(invited_students)
    attending_students = [student_id for student_id, answer in students_answers if answer]

    per_person_cost = 2 + 3.5 + 20.25 + 8  # Juice, Salad, Main dish, Dessert
    total_attendees = len(attending_students)
    snack_cost = ceil(total_attendees / 4) * 6  # One snack plate per 4 persons
    total_price = total_attendees * per_person_cost + snack_cost

    # Apply discount if more than 8 attendees
    if total_attendees > 8:
        total_price *= 0.85  # Apply 15% discount

    logger.info(f"Number of people attending: {total_attendees}, Total Price: ${total_price:.2f}")
