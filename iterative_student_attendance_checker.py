
total_days = 0
perfect_attendance = 5
incomplete_attendance = 0
complete_attendance = 0

student_num = int(input("Enter the amount of students: "))
print("")

for i in range(student_num):
    i = i + 1
    attendance = int(input(f"Enter the attendance of student {i}: "))
    if attendance < perfect_attendance:
        incomplete_attendance = incomplete_attendance + 1
    else:
        complete_attendance = complete_attendance + 1
    total_days = total_days + attendance

def calculate_average(total_days, student_num):
    m = total_days / student_num
    return m
average = calculate_average(total_days, student_num)

def student_report(average, complete_attendance, incomplete_attendance, student_num):
    print("=" * 40)
    print("      CLASS ATTENDANCE REPORT")
    print("=" * 40)
    print(f"Average days attended: {average:.2f}")
    print(f"Perfect attendance: {complete_attendance}")
    print(f"Incomplete attendance: {incomplete_attendance}")
    print(f"Number of students: {student_num}")

student_report(average, complete_attendance, incomplete_attendance, student_num)














