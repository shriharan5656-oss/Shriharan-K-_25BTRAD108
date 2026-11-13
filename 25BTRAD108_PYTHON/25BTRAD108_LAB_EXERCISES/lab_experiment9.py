# Student Grading System

# Storing student names and marks in a dictionary
students_marks = {
    "Arun": 92,
    "Priya": 78,
    "Rahul": 85,
    "Anita": 60,
    "Kiran": 45
}

print("--- Student Grading Results ---")
print(f"{'Student Name':<15} {'Marks':<10} {'Grade':<10}")
print("-" * 35)

for name, marks in students_marks.items():
    # Calculating grades using conditional statements
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F (Fail)’

    print(f"{name:<15} {marks:<10} {grade:<10}”)
