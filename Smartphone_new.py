from Address_new import CompanyAddr, CustomerAddr


class SmartPhone:

    def __init__(self):
        self.addr_list = []
        
    def inputCompanyAddr(self):
        print("회사 연락처 입력")
        name = input("이름 입력: ").strip()
        phone = input("전화번호 입력: ").strip()
        email = input("이메일 입력: ").strip()
        address = input("주소입력: ").strip()
        birthday = input("생일입력(예: 1990-01-01): ").strip()
        company = input("회사명입력: ").strip()
        department = input("부서명 입력: ").strip()
        position = input("직급 입력: ").strip()
        return CompanyAddr(name, phone, email, address, birthday, company, department, position)

    def inputCustomerAddr(self):
        print("거래처 연락처 입력")
        name = input("이름 입력: ").strip()
        phone = input("전화번호 입력: ").strip()
        email = input("이메일 입력: ").strip()
        address = input("주소입력: ").strip()
        birthday = input("생일입력(예: 1990-01-01): ").strip()
        company = input("거래처명입력: ").strip()
        item = input("품목이름 입력: ").strip()
        position = input("직급 입력: ").strip()
        return CustomerAddr(name, phone, email, address, birthday, company, item, position)

    def addAddr(self, addr):
        if len(self.addr_list) >= 10:
            print("연락처가 가득 찼습니다.")
            return

        self.addr_list.append(addr)
        print("연락처가 저장되었습니다.")

    def printAddr(self, addr):
        addr.print_info()

    def printAllAddr(self):
        if not self.addr_list:
            print("저장된 연락처가 없습니다.")
            return
        for idx, addr in enumerate(self.addr_list, 1):
            print(f"[{idx}]")
            self.printAddr(addr)

    def searchAddr(self, name):
        target = None
        for addr in self.addr_list:
            if addr.name == name:
                print(f"{name}님의 검색 결과")
                self.printAddr(addr)
                return
            target = name
        if not target:
            print(f"{name}님의 검색 결과가 없습니다.")

    def deleteAddr(self, name):
        for addr in self.addr_list:
            if addr.name == name:
                self.addr_list.remove(addr)
                print(f"{name}님의 연락처가 삭제되었습니다.")
                return
        print(f"{name}의 연락처가 없습니다.")

    def editAddr(self):
        name = input("수정할 이름을 입력하세요: ").strip()

        for addr in self.addr_list:
            if addr.name == name:
                print(f"{name}님의 정보를 수정합니다.")
                addr.phone = input("새 전화번호 입력: ").strip()
                addr.email = input("새 이메일 입력: ").strip()
                addr.address = input("새 주소입력: ").strip()

                if isinstance(addr, CompanyAddr):
                    print("회사 세부 정보 수정")
                    addr.company = input("신규 회사명 입력: ").strip()
                    addr.department = input("신규 부서명 입력: ").strip()
                    addr.position = input("신규 직급 입력: ").strip()

                elif isinstance(addr, CustomerAddr):
                    print("거래처 세부 정보 수정")
                    addr.company = input("신규 회사명 입력: ").strip()
                    addr.item = input("신규 품목이름 입력: ").strip()
                    addr.position = input("신규 직급 입력: ").strip()

                print(f"{name}님의 정보가 수정되었습니다.")
                return
        print(f"{name}님의 연락처가 없습니다.")     