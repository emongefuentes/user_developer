import csv
from actions import all_students

def export_data():
    if not all_students:
        print("No students available to export.")
        return
    
    file_name = "students_data.csv"
    fieldnames = ["student_name", "group", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"]
    
    try:
        with open(file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_students)
            
        print(f"Data has been successfully exported to {file_name}.")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

def import_data():
    file_name = "students_data.csv"
    try:
        with open(file_name, mode='r') as file: 
            reader = csv.DictReader(file)
            for row in reader:
                if not all(k in row for k in ["student_name", "group", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"]):
                    print("Error: Invalid CSV format. Skipping row.")
                    continue
                
                student = {
                    "student_name": row["student_name"],
                    "group": row["group"],
                    "spanish_grade": int(row["spanish_grade"]),
                    "english_grade": int(row["english_grade"]),
                    "social_studies_grade": int(row["social_studies_grade"]),
                    "science_grade": int(row["science_grade"])
                }
                all_students.append(student)
                
        print(f"Data has been successfully imported from {file_name}.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist")
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
