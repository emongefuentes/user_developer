all_students = []

class Student:
    def __init__(self, name, group, spanish, english, social_studies, science):
        self.name = name
        self.group = group
        self.spanish_grade = spanish
        self.english_grade = english
        self.social_studies_grade = social_studies
        self.science_grade = science

def add_student_info():
    print("please add the next information")
    name = input("Full name: ")
    group = input("group or section: ")

    grades = {}
    subjects = ["spanish", "English", "social_studies", "Science"]

    for subject in subjects:
        while True:
            try:
                number = int(input(f"{subject} grade: "))
                if 0 <= number <= 100:
                    grades[subject.lower()] = number
                    break
                else:
                    print("please enter a number between 0 and 100")
            except ValueError:
                print("Error, only numbers are allowed")

    student_obj = Student(
        name,
        group,
        grades["spanish"],
        grades["english"],
        grades["social_studies"],
        grades["science"]
    )

    all_students.append(student_obj)
    print("This student has been added correctly")

def show_students():
    if not all_students:
        print("no students have been added yet")
        return

    print("\n List of all students: ")
    for student in all_students:
        print(f"Name: {student.name}, Group: {student.group}")
        print(f"Spanish grade: {student.spanish_grade}")
        print(f"English grade: {student.english_grade}")
        print(f"Social Studies grade: {student.social_studies_grade}")
        print(f"Science grade: {student.science_grade}")
        print("-" * 30)

def calculate_average(student):
    return (
        student.spanish_grade +
        student.english_grade +
        student.social_studies_grade +
        student.science_grade
    ) / 4

def show_top_students():
    if len(all_students) < 3:
        print("Not enough students to display top 3.")
        return

    students_with_averages = [
        (student, calculate_average(student)) for student in all_students
    ]
    top_students = sorted(students_with_averages, key=lambda s: s[1], reverse=True)[:3]

    print("\nTop 3 students with the best scores: ")
    for i, (student, avg) in enumerate(top_students, start=1):
        print(f"{i}. Name: {student.name}, Average Grade: {avg:.2f}")

def show_averages():
    if not all_students:
        print("no students have been added yet")
        return
    print("\nAverage grade of each student:")
    for student in all_students:
        average = calculate_average(student)
        print(f"Name: {student.name}, Average Grade: {average:.2f}")