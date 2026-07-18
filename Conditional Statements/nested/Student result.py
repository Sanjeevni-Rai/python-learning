marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 40:
    if attendance >= 75:
        print("Pass")
    else:
        print("Attendance Short")
else:
    print("Fail")