from Address import Addr


class SmartPhone:

    def __init__(self):
        self.addr_list = []
        self.MAX_LIST = 10

    def inputAddrData(self):
        name = input("이름을 입력하세요: ").strip()
        phone_num = input("전화번호를 입력하세요: ").strip()
        email = input("이메일을 입력하세요: ").strip()
        address = input("주소를 입력하세요: ").strip()
        group = input("그룹(친구/가족)을 입력하세요: ").strip()
        return Addr(name, phone_num, email, address, group)

    def addAddr(self, addr):
        if len(self.addr_list) >= self.MAX_LIST:
            print("데이터가 가득 찼습니다.")
            return
        self.addr_list.append(addr)
        print("데이터가 저장되었습니다.")

    def printAddr(self, addr):
        addr.print_info()

    def printAllAddr(self):
        if not self.addr_list:
            print(f"등록된 연락처가 없습니다.")
            return
        
        for idx, addr in enumerate(self.addr_list, 1):
            print(f"[{idx}]")
            self.printAddr(addr)

    def searchAddr(self, word):
        found = False
        for addr in self.addr_list:
            if addr.name == word:
                self.printAddr(addr)
                found = True
                return
        if not found:
            print(f"{word}이 주소록에 없습니다.")

    def deleteAddr(self, word):
        for addr in self.addr_list:
            if addr.name == word:
                self.addr_list.remove(addr)
                print(f"{word}님 주소록에서 삭제되었습니다.")
                return
        print(f"{word}님 주소록에 없습니다.")

    def editAddr(self, word):
        for addr in self.addr_list:
            if addr.name == word:
                print(f"{word}님의 정보를 수정합니다.")
                new_phone_num = input(f"신규 폰번호 [{addr.phone_num}]: ").strip()
                new_email = input(f"신규 이메일 [{addr.email}]: ").strip()
                new_address = input(f"신규 주소 [{addr.address}]: ").strip()
                new_group = input(f"신규 그룹 [{addr.group}]: ").strip()
                if new_phone_num:
                    addr.phone_num = new_phone_num
                if new_email:
                    addr.email = new_email
                if new_address:
                    addr.address = new_address
                if new_group:
                    addr.group = new_group

                print(f"{word}님의 정보가 수정되었습니다.")
                return
        print(f"{word}님은 주소록에 없습니다.")