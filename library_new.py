from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """도서관 최상위 추상 클래스"""
    total_items = 0
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_loaned = False  #대출 가능 여부 false가 가능
        self.borrower = None    #대출자 이름
        LibraryItem.total_items += 1

    @abstractmethod
    def loan_period(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def checkout(self, name):
        if self.is_loaned:
            print(f"{self.title}은(는) 이미 {self.borrower}님이 대출중입니다.")
            return False
        self.is_loaned = True
        self.borrower  = name
        print(f"{name}님, '{self.title}' 대출완료! (대출기간{self.loan_period()}일)")
        return True

    def return_item(self):
        if not self.is_loaned:
            print(f"'{self.title}'은(는) 대출 상태가 아닙니다.")
        print(f"{self.borrower}님이 '{self.title}'을(를) 반납했습니다.")
        self.is_loaned = False
        self.borrower = None
        #prev_borrower = self.borrower #대여자 이름을 저장해놨으나 미리 찍어도 되네.


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def loan_period(self):
        return 14

    def info(self):
        return f"[도서]{self.title} / {self.author} / {self.pages}쪽"


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, minutes):
        super().__init__(title, item_id)
        self.director = director
        self.minutes = minutes

    def loan_period(self):
        return 7

    def info(self):
        return f"[DVD]{self.title} / {self.author} / {self.minutes}분"


class Magajin(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def loan_period(self):
        return 3

    def info(self):
        return f"[잡지]{self.title} / {self.issue}호"
    

class Library():
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"'{item.title}' 등록 완료 (총 {len(self.items)}개)")

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
        print("-"*56)

    def report(self):
        kinds = {}
        for item in self.items:
            name = type(item).__name__
            kinds[name] = kinds.get(name, 0) + 1

        sorted_kinds = sorted(kinds, key=lambda x: kinds[x], reverse=True)
        loaned_count = len([i for i in self.items if i.is_loaned])

        print("-"*50)
        print(f"{'종류별등록현황':^50}")
        print("-"*50)

        for k in sorted_kinds:
            print(f"{k:<15}{kinds[k]:>2}개")

        print("-"*56)
        print(f"{'대출중':<6}{loaned_count:>2}개")
        print(f"{'전체등록':<6}{LibraryItem.total_items:>2}개 (클래스변수)")
        print("-"*56)
