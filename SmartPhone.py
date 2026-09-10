from Address import Addr


class SmartPhone:
    MAX_SIZE = 10

    def __init__(self):
        self.addr = []
      
    def inputAddrData(self):
        print()
        name = input("이름을 입력하세요: ").strip()
        phone_number = input("전화번호를 입력하세요: ").strip()
        email = input("이메일을 입력하세요: ").strip()
        address = input("주소를 입력하세요: ").strip()
        group = input("그룹(친구/가족)을 입력하세요: ").strip()
        return Addr(name, phone_number, email, address, group)

    def addAddr(self, addr):
        if  len(self.addr) >= self.MAX_SIZE:
            print("연락처가 가득 찼습니다.")
            return
        self.addr.append(addr)
        print("연락처가 저장되었습니다.")

    def printAddr(self, addr, index=None):
        if index is not None:
            print(f"[{index}]")
            print(addr)

    def printAllAddr(self):
        if not self.addr:
            print("저장된 연락처가 없습니다.")
            return
        for i, addr in enumerate(self.addr, 1):
            self.printAddr(addr, i)

    def searchAddr(self, word):
        #found = [addr for addr in self.addr if addr.name == word]
        found = False
        for i, addr in enumerate(self.addr, 1):
            if addr.name == word:
                self.printAddr(addr, i)
                found = True
                return
        if not found:
            print("검색 결과가 없습니다.")

    def deleteAddr(self, word):
        found = False
        for addr in self.addr:
            if addr.name == word:
                self.addr.remove(addr)
                print(f"{addr.name}님이 삭제되었습니다.")
                found = True
                return
        if not found:
            print("검색 결과가 없습니다.")

    def editAddr(self, word):
        for addr in self.addr:
            if addr.name == word:
                print(f"{addr.name}님의 정보를 수정합니다.(Enter입력시 기존 정보유지)")
                new_name = input(f"새로운 이름 {addr.name}: ").strip()
                new_phone_number = input(f"신규 번호 {addr.phone_number}: ").strip()
                new_email = input(f"신규 이메일 {addr.email}: ").strip()
                new_address = input(f"신규 주소 {addr.address}: ").strip()
                new_group = input(f"신규 그룹 {addr.group}: ").strip()
                if new_name:
                    addr.name = new_name
                if new_phone_number:
                    addr.phone_number = new_phone_number
                if new_email:
                    addr.email = new_email
                if new_address:
                    addr.address = new_address
                if new_group:
                    addr.group = new_group
                print(f"{addr.name}님의 정보가 수정되었습니다.")
                return
            
        print("검색결과가 없습니다.")