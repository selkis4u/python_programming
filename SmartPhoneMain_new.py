from Address_new import Addr, CustomerAddr,CompanyAddr
from SmartPhone_new import SmartPhone


class SmartPhoneMain:


    def __init__(self):
        self.addr_book = SmartPhone()
                

    @staticmethod
    def PrintMenu():
        print("Contact Manager")
        print("-"*30)
        print("1.연락처 등록(회사)")
        print("2.연락처 등록(거래처)")
        print("3.모든 연락처 출력")
        print("4.연락처 검색")
        print("5.연락처 삭제")
        print("6.연락처 수정")
        print("7.프로그램 종료")
        print("-"*30)

    def add_addr(self):
        a = CompanyAddr("송용석", "010-111-1111", "email@email", "대구 북구", "1973-10-31", "네이버", "개발팀", "부장")
        self.addr_book.addAddr(a)

    def start(self):
                
        while True:
            
            self.PrintMenu()
            choice_menu = input("원하는 작업을 선택하세요(1~7): ").strip()

            if choice_menu == "1":
                addr = self.addr_book.inputCompanyAddr()
                self.addr_book.addAddr(addr)

            elif choice_menu == "2":
                addr = self.addr_book.inputCustomerAddr()
                self.addr_book.addAddr(addr)

            elif choice_menu =="3":
                self.addr_book.printAllAddr()

            elif choice_menu == "4":
                name = input("검색할 이름을 입력하세요: ").strip()
                self.addr_book.searchAddr(name)

            elif choice_menu == "5":
                name = input("삭제할 이름을 입력하세요: ").strip()
                self.addr_book.deleteAddr(name)

            elif choice_menu == "6":
                self.addr_book.editAddr()

            elif choice_menu == "7":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못선택하셨습니다. 1~7번중 선택하세요.")

if __name__ == "__main__":
    app = SmartPhoneMain()
    app.add_addr()
    app.start()