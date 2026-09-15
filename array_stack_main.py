from array_stack import ArrayStack


def main():
    stack = ArrayStack()

    #원소 "a" 삽입
    print("Inserted item: a")
    stack.push("a")
    stack.print_stack()

    #원소 "b" 삽입
    print("Inserted item: b")
    stack.push("b")
    stack.print_stack()

    #원소 "c" 삽입
    print("Inserted item: c")
    stack.push("c")
    stack.print_stack()

    #원소 "c"삭제
    print("delete item: c")
    stack.delete()
    stack.print_stack()

if __name__ == "__main__":
    main()