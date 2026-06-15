# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

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