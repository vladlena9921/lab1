groupmates = [
  {
    "name": "One",
    "group": "1",
    "age": 20,
    "marks": [4, 3, 5, 5, 4]
  },
  {
    "name": "Two",
    "group": "1",
    "age": 18,
    "marks": [3, 2, 3, 4, 3]
  },
  {
    "name": "Three",
    "group": "1",
    "age": 20,
    "marks": [3, 5, 4, 3, 5]
  },
  {
    "name": "Four",
    "group": "1",
    "age": 19,
    "marks": [5, 5, 5, 4, 5]
  },
  {
    "name": "Five",
    "group": "1",
    "age": 18,
    "marks": [5, 5, 5, 5, 5]
  }
]

def count_mark(students,mark):
    print ("name".ljust(15), "group".ljust(8), "age".ljust(8), "marks".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["group"].ljust(8), str(student["age"]).ljust(8), str(student["marks"]).ljust(20))

need = int(input('Input :'))

count_mark(groupmates,need)
