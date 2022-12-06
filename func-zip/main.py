# Python Zip Function
# Inspired by: Python zip() Function: https://www.w3schools.com/python/ref_func_zip.asp

import goodies

print("\n\n")
goodies.echo_badge()

students = ["Foo Alex", "Sam Hamoon", "Bob Romiz"]
major = ["Literature", "DH", "Ecocriticism", "Ling"]
grade = ["A", "B", "C"]

school = zip(students, major, grade)
# print(list(school))

s, m, g = zip(*school)  #! Notice the unpacking operator *
print(s, m, g)
