import sys

course1 = sys.argv[1]
marks1 = sys.argv[2]
course2 = sys.argv[3]
marks2 = sys.argv[4]
course3 = sys.argv[5]
marks3 = sys.argv[6]

total_marks = int(marks1) + int(marks2) + int(marks3)
average_marks = total_marks / 3

print("\n-- Student Marks Report ---")
print(f"Course: {course1}, Marks: {marks1}")
print(f"Course: {course2}, Marks: {marks2}")
print(f"Course: {course3}, Marks: {marks3}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print("largest marks:")
print(max(int(marks1), int(marks2), int(marks3)))
print("smallest marks:")
print(min(int(marks1), int(marks2), int(marks3)))