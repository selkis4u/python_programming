todos = []

prompt = """
1. 할일추가
2. 할일삭제
3. 목록보기
4. 검색하기
5. 종료
"""

while True:
    print(prompt)

    choice = int(input("번호를 선택하세요: "))
    if choice == 1:
        input_todo = input("할일을 입력하세요: ")
        todos.append(input_todo)
        print(f"'{input_todo}' 추가했습니다.(현재 {len(todos)}개)")

    elif choice == 2:
        if len(todos) > 0:
            for i, todo in enumerate(todos, 1):
                print(f"{i:2}. {todo}")
        
            del_todo = int(input("삭제할 번호: "))
            if 1 <= del_todo <= len(todos):
                removed = todos.pop(del_todo-1)
                print(f"'{removed}' 삭제하였습니다.(남은 {len(todos)}개)")
            else:
                print("없는 번호입니다")
        else:
            print("삭제할 일이 없습니다.")

    elif choice == 3:
        print("="*30)
        print(f"{'할일목록':^30}")
        print("="*30)
        if len(todos) > 0:
            for i, todo in enumerate(todos, 1):
                print(f"{i:2}. {todo}")
        else:
            print("등록된 할 일이 없습니다.")
        print("-"*30)
        print(f"총 {len(todos)}개")
        print("-"*30)
        
    elif choice == 4:
        word = input("검색할 단어: ")
        found = [t for t in todos if word in t]
        print(f"'{word}'검색 결과: {len(found)}개")
        for i, todo in enumerate(found, 1):
            print(f"{i:2}. {todo}")
    

    elif choice == 5:
        print("프로그램을 종료합니다.")
        break

    else:
        print("1~5중에서 골라 주세요.")