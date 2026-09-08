class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            print(f"'{self.title}'이미 대출중입니다.")
            return False
        self.is_borrowed = True
        print(f"'{self.title}' 대출 완료 되었습니다.")
        return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' 대출 상태가 아닙니다.")
            return False
        self.is_borrowed = False
        print(f"'{self.title}' 반납 완료하였습니다.")
        return True

class Library:

    def __init__(self):
        self.books =[]

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"'{title}' '{author}' 등록되었습니다.")

    def show_books(self):
        if not self.books:
            print("등록된 도서가 없습니다.")
            return
        print("="*50)
        print(f"{'번호':<5}{'제목':<10}{'저자':>10}{'상태':>15}")
        print("-"*50)
        for i, b in enumerate(self.books, 1):
            status = "대출중" if b.is_borrowed else "대출가능"
            print(f"{i:<5}{b.title:<10}{b.author:>10}{status:>15}")
        print("="*50)

    def search_books(self, word):
        word = word.strip()
        if not word:
            return[]
        return [b for b in self.books if word in b.title or word in b.author]

    def _find_book(self,title):
        return next((b for b in self.books if title == b.title), None)

    def borrow_book(self, title):
        book = self._find_book(title)
        if not book:
            print(f"'{title}' 검색한 도서가 없습니다.")
            return
        book.borrow_book()

    def return_book(self, title):
        book = self._find_book(title)
        if not book:
            print(f"'{title}' 검색한 도서가 없습니다.")
            return
        book.return_book()

def main():

    library = Library()

    #초기 테스트 도서
    library.add_book("점프 투 파이썬", "박응용")
    library.add_book("혼자 공부하는 파이썬", "신윤수")

    while True:
        print("\n [ 도서관 대출 관리 시스템]")
        print(" 1. 도서 등록 2. 전체 목록 3. 도서 검색")
        print(" 4. 도서 대출 5. 도서 반납 0. 종료")
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            title = input("도서 제목: ").strip()
            author = input("도서 저자: ").strip()
            if title and author:
                library.add_book(title,author)
            else:
                print("도서 제목과 도서 저자를 모두 입력하세요.")

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            word = input("검색어(제목/저자): ").strip()
            results = library.search_books(word)
            if not results:
                print("검색 결과가 없습니다.")
            else:
                print(f"총 {len(results)}건 검색되었습니다.")
                for i, b in enumerate(results, 1):
                    status = "대출중" if b.is_borrowed else "대출가능"
                    print(f"{i}.{b.title}{b.author} - {status}")

        elif choice == "4":
            title = input("도서 제목: ").strip()
            library.borrow_book(title)

        elif choice == "5":
            title = input("도서 제목: ").strip()
            library.return_book(title)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못입력하셨습니다. 메뉴 번호를 다시 눌러주세요.")

if __name__ == "__main__":
    main()