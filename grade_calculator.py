"""
grade_calculator.py
--------------------
A small utility to calculate and analyze student grades for a single course.
"""
from typing import Dict, List, Tuple

GRADE_SCALE = {
    "A": (90.0, 100.0),
    "B": (80.0, 89.99),
    "C": (70.0, 79.99),
    "D": (60.0, 69.99),
    "F": (0.0, 59.99),
}

student_grades: Dict[str, List[float]] = {
    "Alice":   [40, 55, 7],
    "Bob":     [92, 88, 95],
    "Charlie": [75, 80, 82],
}

def calculate_student_averages(grades_by_student: Dict[str, List[float]]) -> Dict[str, float]:
    return {s: (sum(g)/len(g) if g else 0.0) for s, g in grades_by_student.items()}

def letter_from_score(score: float) -> str:
    for letter, (low, high) in GRADE_SCALE.items():
        if low <= score <= high:
            return letter
    return "A" if score > 100 else "F"

def determine_letter_grades(averages_by_student: Dict[str, float]) -> Dict[str, str]:
    return {s: letter_from_score(a) for s, a in averages_by_student.items()}

def find_top_performer(averages_by_student: Dict[str, float]) -> Tuple[str, float]:
    if not averages_by_student:
        return ("", 0.0)
    top_student = max(averages_by_student, key=lambda s: averages_by_student[s])
    return (top_student, averages_by_student[top_student])

def compute_class_statistics(averages_by_student: Dict[str, float], letter_map: Dict[str, str]):
    if not averages_by_student:
        return (0.0, 0)
    class_avg = sum(averages_by_student.values()) / len(averages_by_student)
    num_passed = sum(1 for l in letter_map.values() if l in {"A", "B", "C"})
    return (class_avg, num_passed)

def print_report(grades_by_student, averages_by_student, letter_map, top_student, top_avg, class_avg, num_passed):
    print("=" * 60)
    print("STUDENT GRADE REPORT")
    print("=" * 60)
    print("\nRaw Grades:")
    for student, grades in grades_by_student.items():
        print(f"  - {student:10s}: {grades}")
    print("\nAverages & Letters:")
    for student in sorted(averages_by_student):
        avg = averages_by_student[student]
        letter = letter_map[student]
        print(f"  - {student:10s}: average={avg:6.2f}  letter={letter}")
    print("\nTop Performer:")
    print(f"  - {top_student} with an average of {top_avg:.2f}")
    print("\nClass Statistics:")
    print(f"  - Overall class average: {class_avg:.2f}")
    print(f"  - Students passed (C or better): {num_passed} / {len(averages_by_student)}")
    print("=" * 60)

def main() -> None:
    student_averages = calculate_student_averages(student_grades)
    student_letter_grades = determine_letter_grades(student_averages)
    top_name, top_avg = find_top_performer(student_averages)
    class_avg, num_passed = compute_class_statistics(student_averages, student_letter_grades)
    print_report(student_grades, student_averages, student_letter_grades, top_name, top_avg, class_avg, num_passed)

if __name__ == "__main__":
    main()