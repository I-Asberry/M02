#Isaac Asberry
#Dean's List/Honor Roll Verifier
#This program will accept user inputs for first and last name, along with their GPA, to output wether they made Dean's List or Honor Roll or none

last_name = input("Last name: ")

while last_name != "ZZZ" and last_name != "zzz":  
    first_name = input("First name: ")
    stu_gpa = float(input("GPA: ")) 

    if stu_gpa >= 3.5:
        print("""You have made the Dean's List! \nType "ZZZ" or "zzz" to quit.""")

    elif stu_gpa >= 3.25:
        print("""You have made the Honor Roll! \nType "ZZZ" or "zzz" to quit.""")

    else:
        print("""You have not made the Dean's List or Honor Roll. \nType "ZZZ" or "zzz" to quit.""")
    
    last_name = input("Last name: ")