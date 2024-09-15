list= [1, 62, 32, 89]
print(list[-4:-1])

#Dictionary

student= {
    'firstName':'aaa',
    'surname':'bbb',
    'schoolName':'school',
    'grade':10,
    'marks':[50,60,45,85],
    'attendance':'87%',
    'formtutor':'Mr Smith'
}
print(student)
print(student['firstName'])

#Keys
print(student.keys())
#Values
print(student.values())

for x in student.keys():
    print(x, student[x])

#Checking if a key exists

if 'middlename' in student:
    print('exists')
else:
    print('Does not exist')

student['middlename']='Dev'

print(student)

#Deleting a key and value pair

del(student['formtutor'])

print(student)

print(student['marks'][2])