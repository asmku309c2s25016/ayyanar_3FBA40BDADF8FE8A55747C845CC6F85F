class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
students = [
  Student("Maharaja", "A122", 7.0),
  Student("Aananth", "A125", 8.1),
  Student("Ayyanar", "A126", 9.2),
  Student("Dhoni", "A127", 9.3),
]

sorted_students = sort_students(students)

# Print the sorted students
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
