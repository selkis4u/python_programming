from Address import Addr
from SmartPhone import SmartPhone


class SmartPhoneMain:

    def __init__(self):
        self.addr = SmartPhone()

    def start(self):
        add1 = Addr("송용석", "010-1111-1111", "se@nam.com", "대구", "가족")
        add2 = Addr("고길동", "010-2222-2222", "go@nam.com", "서울", "가족")
        self.addr.addAddr(add1)
        self.addr.addAddr(add2)

    def printMenu(self):
        print("-"*30)
        print("주소관리메뉴")
        print("-"*30)
        print("1.연락처등록")
        print("2.모든 연락처 출력")
        print("3.연락처 검색")
        print("4.연락처 삭제")
        print("5.연락처 수정")
        print("6.프로그램 종료")
        print("-"*30)

    def main(self):
        while True:
            self.printMenu()
            choice = input("원하는 작업을 선택하세요(1~6): ").strip()

            if choice == "1":
                new_addr = self.addr.inputAddrData()
                self.addr.addAddr(new_addr)

            elif choice == "2":
                self.addr.printAllAddr()

            elif choice == "3":
                name = input("검색할 성함을 입력해주세요: ").strip()
                self.addr.searchAddr(name)

            elif choice == "4":
                name = input("삭제할 성함을 입력해주세요: ").strip()
                self.addr.deleteAddr(name)

            elif choice == "5":
                name = input("수정하실 성함을 입력해주세요: ").strip()
                self.addr.editAddr(name)

            elif choice == "6":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못입력하셨습니다.(1~6번 메뉴를 선택해주세요.)")

if __name__ == "__main__":
    app = SmartPhoneMain()
    app.start()
    app.main()