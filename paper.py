def gradingStudents(grades):
    nl=[]
    for grade in grades:
        if grade > 37 and grade % 5 > 2:
            grade = grade + 5 - (grade % 5)
            nl.append(grade)
        elif grade<38:
            nl.append(grade)

    return nl


grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
result = gradingStudents(grades)
print(result)