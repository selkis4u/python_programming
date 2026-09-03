# [저장 패턴] 리스트 -> 파일 (각 요소 뒤에 줄바꿈 '\n' 추가)
todos = ["파이썬 복습", "알고리즘 문제 풀이", "장보기"]
with open("todo.txt", "w", encoding="utf-8") as f:
    for task in todos:
        f.write(task + "\n")

# [복원 패턴] 파일 -> 리스트 (strip()으로 줄바꿈 '\n' 제거 후 append)
loaded_todos = []
with open("todo.txt", "r", encoding="utf-8") as f:
    for line in f:
        loaded_todos.append(line.strip())

print(loaded_todos)  # ['파이썬 복습', '알고리즘 문제 풀이', '장보기']