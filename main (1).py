class Student:
  def __init__(self,name,     roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(students_list):
  #sort the list of students in desceding order of CGPA
  sorted_students=sorted(students_list, key=lambda student:student.cgpa, reverse=True)
#syntax - lamda arg:exp
  return sorted_students
#Example useage:
students = [Student("ammu","A123",7.8), 
Student("siva","A124",8.9), 
Student("mathan","A121",9.1), Student("muthu","A122",9.9),]
sorted_students=sort_students(students)
#Print the shorted list of student 
for student in sorted_students:
  print("Name:{},Rollnumber{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))