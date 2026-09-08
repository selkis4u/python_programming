from abc import ABC, abstractmethod

class LibraryItem(ABC):
    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_loaned = False
        self.borrower = None
        LibraryItem.total_items += 1

    def checkout(self, name):
        if self.is_loaned:
            print(f"'{self.title}'은(는) 이미 {self.borrower}님이 대출중입니다.")
            return False
        self.is_loaned = True
        self.borrower = name
        print(f"'{name}님' {self.title}' 대출완료!(대출기간 : {self.loan_period()}일)")
        return True

    def return_item(self):
        if not self.is_loaned:
            print(f"'{self.title}'은(는) 대출 상태가 아닙니다.")
            return False
        
        prev_borrower = self.borrower
        self.is_loaned = False
        self.borrower = None
        print(f"{prev_borrower}님이 '{self.title}'을(를) 반납하였습니다.")
        return True

    @abstractmethod
    def loan_period(self):
        pass

    @abstractmethod
    def info(self):
        pass

       
class Book(LibraryItem):
    
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def loan_period(self):
        return 14

    def info(self):
        return f"[도서] {self.title} / {self.author} / {self.pages}쪽"

        
class DVD(LibraryItem):

    def __init__(self, title, item_id, director, minutes):
        super().__init__(title, item_id)
        self.director = director
        self.minutes = minutes

    def loan_period(self):
        return 7

    def info(self):
        return f"[DVD] {self.title} / {self.director} / {self.minutes}분"

    
class Magazine(LibraryItem):
    
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue
        
    def loan_period(self):
        return 3

    def info(self):
        return f"[잡지] {self.title} / {self.issue}호"


class Library():

    def __init__(self, name):
       self.name = name
       self.items= []

    def add(self, item):
        self.items.append(item)
        print(f"'{item.title}'등록 완료(총 {len(self.items)})개")

    def find(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def show_all(self):
        print("="*56)
        print(f"{self.name:^28}")
        print("="*56)
        print(f"{'ID':<6}{'정보':<15}{'상태':>30}")
        print("-"*56)
        for item in self.items:
            state = f"대출중({item.borrower})" if item.is_loaned else "대출가능"
            print(f"{item.item_id:<6}{item.info():<15}{state:>10}")
        print("="*56)

    def report(self):
        print("-"*56)
        print(f"{'종류별등록현황':<28}")
        print("-"*56)

        kinds = {}
        for item in self.items:
            t_name = type(item).__name__
            kinds[t_name] = kinds.get(t_name, 0) + 1
            #if kinds in counts:
            #    counts[kinds] = counts[kinds] + 1
            #else:
            #    counts[kinds] = 1
        sorted_kinds = sorted(kinds.items(), key=lambda x: x[1], reverse=True)

        for k, v in sorted_kinds:
            print(f"{k:<15}{v:>2}개")
        print("-"*56)
        print(f"{'대출중':<6}{len([i for i in self.items if i.is_loaned])}개")
        print(f"{'전체등록':<6}{LibraryItem.total_items:>2}개 (클래스변수)")
        print("-"*56)


if __name__ == "__main__":

    # 도서관 생성 및 초기 자료 등록
    lib = Library("한빛도서관")
    lib.add(Book("파이썬 입문", "B001", "박응용", 480))
    lib.add(Book("자료구조", "B002", "김철수", 320))
    lib.add(DVD("인터스텔라", "D001", "놀란", 169))
    lib.add(Magazine("과학동아", "M001", 9))


    while True:
        print("1.전체목록  2.통계  3.대출  4.반납  0.종료")
        choice = input("번호를 선택하세요: ")

        if  choice == "1":
            lib.show_all()

        elif choice == "2":
            lib.report()

        elif choice == "3":
            item_id = input("대출할 자료 번호: ").upper()
            item = lib.find(item_id)
            
            if item is None:
                print("없는 번호입니다.")
                continue
            user_name = input("대출자 이름: ").strip()
            item.checkout(user_name)

        elif choice == "4":
            item_id = input("반납할 자료 번호: ").strip().upper()
            item = lib.find(item_id)
            if item is None:
                print("없는 번호입니다.")
                continue
            item.return_item()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("없는 메뉴입니다.")