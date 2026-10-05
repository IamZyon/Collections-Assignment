name = input("Enter the students name?\n")
grade1 = int(input("Enter a grade: "))
grade2 = int(input("Enter a grade: "))
grade3 = int(input("Enter a grade: "))
grade4 = int(input("Enter a grade: "))
grade5 = int(input("Enter a grade: "))

print()
print(name)
print()

def gradeFinder():

    grades = ['A', 'B', 'C', 'D', 'F']
    usersGrades = [grade1, grade2, grade3, grade4, grade5]
    total = sum(usersGrades)
    average = total / 5

    if average >= 90:
        grade = grades[0]
    elif average >= 80:
        grade = grades[1]
    elif average >= 70:
        grade = grades[2]
    elif average >= 60:
        grade = grades[3]
    elif average >= 0:
        grade = grades[4]

    print('Average:', average)
    print()
    print('Letter Grade: ', grade)

gradeFinder()