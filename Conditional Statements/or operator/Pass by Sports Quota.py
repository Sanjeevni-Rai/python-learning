marks = int(input("Enter marks: "))
sports = input("Sports Quota? (yes/no): ")

if marks >= 40 or sports == "yes":
    print("Selected")
else:
    print("Rejected")