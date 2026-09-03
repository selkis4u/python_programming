import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end =" ")

# [저장 패턴] 리스트 -> 파일 (각 요소 뒤에 줄바꿈 '\n' 추가)
todos = ["파이썬 복습", "장보기"]
with open("text/todo.txt", "w", encoding="utf-8") as f:
    for task in todos:
        f.write(task + "\n")

# [복원 패턴] 파일 -> 리스트 (strip()으로 줄바꿈 '\n' 제거 후 append)
loaded_todos = []
with open("text/todo.txt", "r", encoding="utf-8") as f:
    for line in f:
        loaded_todos.append(line.strip())

print(loaded_todos)  # ['파이썬 복습', '알고리즘 문제 풀이', '장보기']

# print("로딩", end="...")
# print("완료")

   
# with open("text/새파일.txt", "w", encoding="utf-8") as f:
#     for i in range(1,11):
#         data = "%d번째 줄입니다.\n" %i
#         f.write(data)        

# lines = [f"{i}번째 줄입니다." for i in range(1, 11)]

# with open("새파일.txt", "w", encoding="utf-8") as f:
#    f.write("\n".join(lines))

# f = open("text/새파일.txt", "a", encoding="utf-8")
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

# with open("text/새파일.txt", "r", encoding="utf-8") as f:
#     for i in f:
#         print(i.strip())
#     print(len(i))

# with open("text/foo.txt", "w")as f:
#     f.write("life is too short, i need you")