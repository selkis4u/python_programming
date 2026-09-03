todos =[]

todo_menu = """
1. 할 일 추가
2. 할 일 삭제
3. 목록보기
4. 검색하기
5. 종료
"""

print(todo_menu)

while True:    
    todo_num = int(input("번호를 선택하세요: "))
    if todo_num == 1:
        input_todo = input("할 일을 입력하세요: ")
        todos.append(input_todo)
        print(f"'{input_todo}' 추가했습니다. (현재{len(todos)}개)")
        
    elif todo_num == 2:
        if len(todos) == 0:
            print("삭제할 항목이 없습니다.")
        else: #len(todos) > 0:
            for i, todo in enumerate(todos, 1):
                print(f"{i:>2}. {todo}")
            del_num = int(input("삭제할 번호: "))
            if 1 <= del_num <= len(todos):
                removed = todos.pop(del_num - 1)
                print(f"'{removed}' 삭제했습니다. 남은 {len(todos)}개")
            else:
                print("없는 번호입니다.")
    
    elif todo_num == 3:
        print("*"*30)
        print(f"{'할 일 목록':^30}")
        print("*"*30)
        for i, todo in enumerate(todos, 1):
            print(f"{i:>2}. {todo}") 
        print("-"*30)
        print(f"총 {len(todos):>2}개")
        print("="*30)

    elif todo_num == 4:
        word = input("검색할 단어: ")
        found = [t for t in todos if word in t]
        if found:
            print(f"'{word}' 검색 결과:{len(found)}개")
            for i, t in enumerate(found, 1):
                print(f"{i:>2}. {t}")
        else:
            print(f"'{word}'을(를) 찾을 수 없습니다.")

    elif todo_num == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~5 중에서 골라주세요.")
        print(todo_menu)