student = {'name':'김민준', 'age':20, 'major':'컴퓨터공학'}

print(student)
print(student.get('name'), student.get('age'), student.get('major'))
print(f"항목수: {len(student)}개항목")

student['email'] = 'minjun@example.com'
student['hobbies'] = ['python', 'game']
student['age'] = 21
del student['major']
print(student)
print(f"항목수: {len(student)}")

print(f"{student.get('name')}")
print(f"{student.get('phone')}")
print(f"{student.get('phone', '등록되지않음')}")
print(f"{'email' in student}, {'major' in student}")

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

print("="*34)
print(f"{'PROFILE':^30}")
print("="*34)
print(f"{'이름':<12} {student.get('name'):>18}")
print(f"{'나이':<12} {student.get('age'):>18}")
print(f"{'이메일':<12} {student.get('email'):>18}")
print(f"{'전화':<12} {student.get('phone', '미등록'):>18}")
print("-"*34)
print(f"{'취미':<12} {str(student.get('hobbies')):>18}")
print(f"{'항목수':<12}{len(student):>18}")
print("="*34)