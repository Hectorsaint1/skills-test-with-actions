def calculate_math_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

def calculate_history_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

def process_student(student):
    total = 0

    for grade in student["grades"]:
        total += grade

    average = total / len(student["grades"])

    if average >= 7:
        status = "Approved"
    else:
        status = "Failed"

    print(student["name"])
    print(total)
    print(average)
    print(status)

    print("Processing")
    print("Checking")
    print("Generating report")
    print("Saving")
    print("Done")