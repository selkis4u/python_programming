print ("Hello python")
name = input ("이름을 입력하세요:")
print("안녕하세요 {name}님")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(loaded_todos)  # ['파이썬 복습', '알고리즘 문제 풀이', '장보기']