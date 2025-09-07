"""
grade_calculator.py
--------------------
A small utility to calculate and analyze student grades for a single course.
"""

from typing import Dict, List, Tuple

# Standard grading scale.
# Each letter is mapped to a (low, high) range.
GRADE_SCALE = {
    "A": (90.0, 100.0),
    "B": (80.0, 89.99),
    "C": (70.0, 79.99),
    "D": (60.0, 69.99),
    "F": (0.0, 59.99),
}

# Dictionary to hold student names and their list of grades.
# Keys = student names (str), values = list of grades (float or int).
student_grades: Dict[str, List[float]] = {
    "Alice":   [40, 55, 7],   # intentionally low grades to test "F"
    "Bob":     [92, 88, 95],  # strong grades → should get "A"
    "Charlie": [75, 80, 82],  # middle range → should get "C"
}

def calculate_student_averages(grades_by_student: Dict[str, List[float]]) -> Dict[str, float]:
    """
    Compute the average grade for each student.
    - If a student has no grades, return 0.0 to avoid ZeroDivisionError.
    - Dictionary comprehension makes this concise and efficient.
    """
    return {s: (sum(g) / len(g) if g else 0.0) for s, g in grades_by_student.items()}

def letter_from_score(score: float) -> str:
    """
    Convert a numeric score into a letter grade using GRADE_SCALE.
    - Iterates through the scale until the score fits a range.
    - Handles out-of-range scores: >100 = "A", negative = "F".
    """
    for letter, (low, high) in GRADE_SCALE.items():
        if low <= score <= high:
            return letter
    return "A" if score > 100 else "F"

def determine_letter_grades(averages_by_student: Dict[str, float]) -> Dict[str, str]:
    """
    Map each student's average score to a letter grade.
    Uses the helper function letter_from_score().
    """
    return {s: letter_from_score(a) for s, a in averages_by_student.items()}

def find_top_performer(averages_by_student: Dict[str, float]) -> Tuple[str, float]:
    """
    Identify the student with the highest average score.
    - Uses Python's max() with a custom key (average score).
    - Returns both the name and the score as a tuple.
    """
    if not averages_by_student:
        return ("", 0.0)  # edge case: no students
    top_student = max(averages_by_student, key=lambda s: averages_by_student[s])
    return (top_student, averages_by_student[top_student])

def compute_class_statistics(averages_by_student: Dict[str, float], letter_map: Dict[str, str]):
    """
    Calculate:
    - class_avg: mean of all student averages
    - num_passed: how many earned a passing grade (C or better)
    """
    if not averages_by_student:
        return (0.0, 0)
    class_avg = sum(averages_by_student.values()) / len(averages_by_student)
    num_passed = sum(1 for l in letter_map.values() if l in {"A", "B", "C"})
    return (class_avg, num_passed)

def print_report(grades_by_student, averages_by_student, letter_map, top_student, top_avg, class_avg, num_passed):
    """
    Pretty-print all results to the terminal:
    - Raw grade lists
    - Averages + letter grades
    - Top performer
    - Overall class stats
    """
    print("=" * 60)
    print("STUDENT GRADE REPORT")
    print("=" * 60)

    # Show raw data
    print("\nRaw Grades:")
    for student, grades in grades_by_student.items():
        print(f"  - {student:10s}: {grades}")

    # Show computed averages and letters
    print("\nAverages & Letters:")
    for student in sorted(averages_by_student):
        avg = averages_by_student[student]
        letter = letter_map[student]
        print(f"  - {student:10s}: average={avg:6.2f}  letter={letter}")

    # Top performer summary
    print("\nTop Performer:")
    print(f"  - {top_student} with an average of {top_avg:.2f}")

    # Class statistics summary
    print("\nClass Statistics:")
    print(f"  - Overall class average: {class_avg:.2f}")
    print(f"  - Students passed (C or better): {num_passed} / {len(averages_by_student)}")
    print("=" * 60)

def main() -> None:
    """
    Main program flow:
    1. Calculate averages for each student.
    2. Map averages to letter grades.
    3. Find the top performer.
    4. Compute overall class statistics.
    5. Print a detailed report.
    """
    student_averages = calculate_student_averages(student_grades)
    student_letter_grades = determine_letter_grades(student_averages)
    top_name, top_avg = find_top_performer(student_averages)
    class_avg, num_passed = compute_class_statistics(student_averages, student_letter_grades)
    print_report(student_grades, student_averages, student_letter_grades, top_name, top_avg, class_avg, num_passed)

if __name__ == "__main__":
    main()
