def get_valid_mark(prompt):
    while True:
        try:
            mark = int(input(prompt))
            if mark >= 0 and mark <= 100:
                return mark
            else:
                print("Invalid mark. Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the mark.")

def calculate_average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)
def determine_grade(average):
    if 90 <= average <= 100:
        return "A+"
    elif 80 <= average < 90:
        return "A"
    elif 70 <= average < 80:
        return "B"
    elif 60 <= average < 70:
        return "C"
    elif 50 <= average < 60:
        return "D"
    else:
        return "F"
