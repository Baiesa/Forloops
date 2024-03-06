# 30 students and 5 rows in classroom.
# each row can seat an equal number of students.
# use a for loop with the range function to assing and print a seat number for each student.
# seat numbers should start at 1 and increase sequantially.

total_students = 30
rows = 5 
students_per_row = total_students // rows
for row in range(1, rows +1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row - 1) * students_per_row + seat
        print(f"Row {row} - Seat {seat} - student {seat_number}")

        



