from Address import Addr
from SmartPhone import SmartPhone


class SmartPhoneMain:

    def printMenu(self):
        print("-"*50)
        print("주소관리 메뉴")
        print("-"*50)
        print("1. 연락처등록")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 프로그램 종료")
        print("-"*50)

    def start(self):

        addr_book = SmartPhone()

        #자료 2개 임의 등록
        addr_book.addAddr(Addr("송용석", "010-1111-1111", "a@mail.com", "대구시 북구", "가족"))
        addr_book.addAddr(Addr("강은비", "010-2222-2222", "b@mail.com", "대구시 남구", "친구"))
        while True:
            self.printMenu()
            choice = input("원하는 작업을 선택하세요.(1~6): ").strip()

            if choice == "1":
                new_addr = addr_book.inputAddData()
                addr_book.addAddr(new_addr)

            elif choice == "2":
                addr_book.PrintAllAddr()

            elif choice == "3":
                target_name = input("검색할 사람 이름을 입력하세요: ").strip()
                addr_book.searchAddr(target_name)

            elif choice == "4":
                target_name = input("삭제할 사람 이름을 입력하세요: ").strip()
                addr_book.deleteAddr(target_name)

            elif choice == "5":
                target_name = input("수정할 사람 이름을 입력하세요: ").strip()
                addr_book.editAddr(target_name)

            elif choice == "6":
                print("프로그램을 종료합니다.")
                break

            else:
                print("없는 번호입니다. 다시 선택해주세요.")

if __name__ == "__main__":

    app = SmartPhoneMain()
    app.start()