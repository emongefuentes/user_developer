all_students = []

def add_student_info():
    students_dictionary = {}
    print("please add the next information")
    students_dictionary["student_name"] = input("Full name: ")
    students_dictionary["group"] = input("group or section: ")
    
    subjects = ["spanish", "English" , "social_studies", "Science"]
    
    for subject in subjects:
        while True:
            try:
                number = int(input(f"{subject} grade: "))
                if 0 <= number <= 100:
                    students_dictionary[f"{subject.lower()}_grade"] = number
                    break
                else:
                    print("please enter a number between 0 and 100")
            except ValueError:
                print("Error, only numbers are allowed")
                
    all_students.append(students_dictionary)
    print("This students has been added correctly")
    
def show_students():
    if not all_students:
        print("no students have been added yet")
        return
    
    print("\n List of all students: ")
    for student in all_students:
        print(f"Name: {student['student_name']}, Group: {student['group']}")
        print(f"Spanish grade: {student['spanish_grade']}")
        print(f"English grade: {student['english_grade']}")
        print(f"Social Studies grade: {student['social_studies_grade']}")
        print(f"Science grade: {student['science_grade']}")
        print("-" * 30)

def calculate_average(student):
    return (student["spanish_grade"] + student["english_grade"] +
            student["social_studies_grade"] + student["science_grade"]) / 4

def show_top_students():
    if len(all_students) < 3:
        print("Not enough students to display top 3.")
        return
    students_with_averages = [
        {**student, "average": calculate_average(student)}
        for student in all_students
    ]
    top_students = sorted(students_with_averages, key=lambda s: s["average"], reverse=True)[:3]
    
    print("\nTop 3 students with the best scores: ")
    for i, student in enumerate(top_students, start=1):
        print(f"{i}. name: {student['student_name']}, Average Grade: {student['average']:.2f}")
        
def show_averages():
    if not all_students:
        print("no students have been added yet")
        return
    print("\nAverage grade of each student:")
    for student in all_students:
        average = calculate_average(student)
        print(f"Name: {student['student_name']}, Average Grade: {average:.2f}")           
                    
        