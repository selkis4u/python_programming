# ====================================================
# 1. 개별 책 한 권의 데이터와 상태를 다루는 Book 클래스
# ====================================================
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # 대출 여부 기본값: False (대출 가능 상태)

    def borrow(self):
        """책 대출 처리"""
        if self.is_borrowed:
            print(f"'{self.title}' 도서는 이미 대출 중입니다.")
            return False
        self.is_borrowed = True
        print(f"'{self.title}' 대출이 완료되었습니다.")
        return True

    def return_book(self):
        """책 반납 처리"""
        if not self.is_borrowed:
            print(f"'{self.title}' 도서는 대출 상태가 아닙니다.")
            return False
        self.is_borrowed = False
        print(f"'{self.title}' 반납이 완료되었습니다.")
        return True


# ====================================================
# 2. 책 목록 전체를 관리하고 조작하는 Library 클래스
# ====================================================
class Library:

    def __init__(self):
        self.books = []  # Book 객체들이 보관될 리스트

    def add_book(self, title, author):
        """새 도서 등록"""
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"도서 등록 완료: {title} ({author})")

    def show_books(self):
        """전체 도서 목록 출력"""
        if not self.books:
            print("등록된 도서가 없습니다.")
            return

        print("\n" + "=" * 45)
        print(f"{'번호':<5}{'제목':<15}{'저자':<12}{'상태':<8}")
        print("-" * 45)
        for i, b in enumerate(self.books, 1):
            status = "대출중" if b.is_borrowed else "대출가능"
            print(f"{i:<5}{b.title:<15}{b.author:<12}{status:<8}")
        print("=" * 45)

    def search_books(self, word):
        """제목 또는 저자명으로 도서 검색 (컴프리헨션)"""
        return [
            b for b in self.books if word in b.title or word in b.author
        ]

    def _find_book(self, title):
        """[내부용 메서드] 제목으로 정확한 도서 객체 1개 찾기"""
        return next((b for b in self.books if b.title == title), None)

    def borrow_book(self, title):
        """도서 대출 실행"""
        book = self._find_book(title)
        if not book:
            print(f"'{title}' 도서를 찾을 수 없습니다.")
            return
        book.borrow()

    def return_book(self, title):
        """도서 반납 실행"""
        book = self._find_book(title)
        if not book:
            print(f"'{title}' 도서를 찾을 수 없습니다.")
            return
        book.return_book()


# ====================================================
# 3. 사용자 인터페이스(CLI) 및 루프를 담당하는 main()
# ====================================================
if __name__ == "__main__":
    
    library = Library()

    # 초기 테스트 데이터
    library.add_book("점프 투 파이썬", "박응용")
    library.add_book("혼자 공부하는 파이썬", "신윤수")

    while True:
        print("\n[ 도서관 대출 관리 시스템 ]")
        print("1. 도서 등록  2. 전체 목록  3. 도서 검색")
        print("4. 도서 대출  5. 도서 반납  0. 종료")
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            title = input("도서 제목: ").strip()
            author = input("도서 저자: ").strip()
            if title and author:
                library.add_book(title, author)
            else:
                print("제목과 저자를 모두 입력해야 합니다.")

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            word = input("검색어(제목/저자): ").strip()
            results = library.search_books(word)
            if not results:
                print("검색 결과가 없습니다.")
            else:
                print(f"\n총 {len(results)}건 검색됨:")
                for i, b in enumerate(results, 1):
                    status = "대출중" if b.is_borrowed else "대출가능"
                    print(f" {i}. {b.title} ({b.author}) - {status}")

        elif choice == "4":
            title = input("대출할 도서 제목: ").strip()
            library.borrow_book(title)

        elif choice == "5":
            title = input("반납할 도서 제목: ").strip()
            library.return_book(title)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 메뉴 번호를 확인하세요.")
