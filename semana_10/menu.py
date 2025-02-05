import actions
import data

def show_menu():
    print("Principal Menu")
    while True:
        try:
            option = int(input("""
                               Welcome to the principal menu
                               please choose an option
                               1. add a new student
                               2. Read the information of every student
                               3. Top 3 with the est score
                               4. look the average of each student
                               5. Export the data
                               6. import data from a csv File
                               7. finish
                               """))
        except ValueError:
            print("invalid option. Add a number between 1 or 7.")
            continue
        
        if option == 1:
            actions.add_student_info()
        elif option == 2:
            actions.show_students()
        elif option == 3:
            actions.show_top_students()
        elif option == 4:
            actions.show_averages()   
        elif option == 5:
            data.export_data()
        elif option == 6:
            data.import_data()
        elif option == 7:
            print("thank you for using our app, feel free to come back any time!!")
            break
        else:
            print("invalid option, please insert a number between 1 and 7")
            
                        