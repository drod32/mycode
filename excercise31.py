#!/usr/bin/env python3


wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

print(wordbank)

num = input("number between zero and 20 \n>")
student_name = tlgstudents[int(num)]
print(student_name)

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")

