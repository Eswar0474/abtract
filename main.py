from grade import get_valid_mark, calculate_average, determine_grade
student_name = input("Enter student name: ")
print("\nEnter marks for the following subjects (0-100):")
marks = []
subjects = ["DS", "Python", "Java", "SQL", "Computer hardware and networking"]
for subject in subjects:
    mark = get_valid_mark(f"Enter mark for {subject}: ")
    marks.append(mark)
average_marks = calculate_average(marks)
grade = determine_grade(average_marks)
print(f"Student Name: {student_name}\nMarks: {sum(marks)}\nAverage Marks: {average_marks}\nGrade: {grade}")

