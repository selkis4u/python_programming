from Address_new import Addr, CompanyAddr, CustomerAddr
from Smartphone_new import SmartPhone


class SmartPhoneMain:

    def printMenu(self):
        print("-"*50)
        print("Contact Manager")
        print("-"*50)
        print("1. 연락처 등록(회사)")
        print("2. 연락처 등록(거래처)")
        print("3. 모든 연락처 출력")
        print("4. 연락처 검색")
        print("5. 연락처 삭제")
        print("6. 연락처 수정")
        print("7. 프로그램 종료")
        print("-"*50)

    def start(self):

        addr_book = SmartPhone()

        #자료 2개 임의 등록
        #addr_book.input_company("송용석", "010-1111-1111", "a@mail.com", "대구시 북구", "1973-10-31", "네이버", "기획", "부장")
        #addr_book.addAddr(Addr("강은비", "010-2222-2222", "b@mail.com", "대구시 남구", "친구"))
        while True:
            self.printMenu()
            choice = input("원하는 작업을 선택하세요.(1~7): ").strip()

            if choice == "1":
                new_addr = addr_book.input_company()
                addr_book.addAddr(new_addr)

            elif choice == "2":
                new_addr = addr_book.input_customer()
            
            elif choice == "3":
                addr_book.PrintAllAddr()

            elif choice == "4":
                target_name = input("검색할 사람 이름을 입력하세요: ").strip()
                addr_book.searchAddr(target_name)

            elif choice == "5":
                target_name = input("삭제할 사람 이름을 입력하세요: ").strip()
                addr_book.deleteAddr(target_name)

            elif choice == "6":
                target_name = input("수정할 사람 이름을 입력하세요: ").strip()
                addr_book.editAddr(target_name)

            elif choice == "7":
                print("프로그램을 종료합니다.")
                break

            else:
                print("없는 번호입니다. 다시 선택해주세요.")

if __name__ == "__main__":

    app = SmartPhoneMain()
    app.start()