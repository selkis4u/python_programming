student = {'name':'김민준', 'age':'20', 'major':'컴퓨터공학'}

print(student)
print(student['name'], student['age'], student['major'])
print(f"항목수 : {len(student)}개 항목")

student['email'] = 'minjun@example.com'
student['hobbies'] = ['python', 'game']
student['age'] = '21'
del student['major']

print(student)
print(f"항목수 : {len(student)}")

print(student.get('name'))
print(student.get('phone', '등록되지않음'))
print('email'in student, 'major'in student)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

print("=" * 34)
print(f"{'PROFILE':^30}")
print("=" * 34)
print(f"{'이름':<12}{student['name']:>10}")
print(f"{'나이':<12}{student['age']:>10}")
print(f"{'이메일':<12}{student['email']:>10}")
print(f"{'전화':<12}{student.get('phone', '미등록'):>10}")
print("-" * 34)
print(f"{'취미':<12}{str(student['hobbies']):>10}")
print(f"항목수 : {len(student)}")
print("=" * 34)
