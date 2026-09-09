from Address_new import Addr, CompanyAddr, CustomerAddr

class SmartPhone:

    def __init__(self):
        self.addr_list = []
        #self.MAX_SIZE = 12

    def input_company(self):
        group = "회사"
        name = input("이름을 입력하세요: ").strip()
        phone_number = input("전화번호를 입력하세요: ").strip()
        email = input("이메일을 입력하세요: ").strip()
        address = input("주소를 입력하세요: ").strip()
        #group = input("친구/가족)을 입력하세요: ").strip()
        birthday = input("생일을 입력하세요(예: 1990-01-01): ").strip()
        company_name = input("회사이름을 입력하세요: ").strip()
        department = input("부서이름을 입력하세요: ").strip()
        level = input("직급을 입력하세요: ").strip()

        return CompanyAddr(name, phone_number, email, address, group, birthday, company_name, department, level)
          

    def input_customer(self):
        group = "거래처"
        name = input("이름을 입력하세요: ").strip()
        phone_number = input("전화번호를 입력하세요: ").strip()
        email = input("이메일을 입력하세요: ").strip()
        address = input("주소를 입력하세요: ").strip()
        #group = input("그룹(친구/가족)을 입력하세요: ").strip()
        birthday = input("생일을 입력하세요(예: 1990-01-01): ").strip()
        customer_name = input("거래처 이름을 입력하세요: ").strip()
        item_name = input("품목 이름을 입력하세요: ").strip()
        level = input("직급을 입력하세요: ").strip()

        addr = CustomerAddr(name, phone_number, email, address, group, birthday, customer_name, item_name, level)
        self.addr_list.append(addr)
        print("데이터가 저장되었습니다.")

    def addAddr(self, addr):
        if len(self.addr_list) >= self.MAX_SIZE:
          print("데이터가 가득찼습니다.")
          return
        self.addr_list.append(addr)
        print("데이터가 저장되었습니다.")

    def printAddr(self, addr):
        addr.print_info()


    def PrintAllAddr(self):
        for i, addr in enumerate(self.addr_list, 1):
            print("모든연락처")
            print(f"\n[{i}]")
            self.printAddr(addr)

    def searchAddr(self, target_name):
        found = [addr for addr in self.addr_list if addr.name == target_name]
        if not found:
            print("검색결과")
            print(f"{target_name}은(는) 목록에 없습니다.")
            return
        for addr in found:
            print("검색결과")
            self.printAddr(addr)        

    def deleteAddr(self, target_name):
        found = [addr for addr in self.addr_list if addr.name == target_name]
        if not found:
            print("삭제결과")
            print(f"{target_name}은(는) 목록에 없습니다.")
            return
        for addr in found:
            self.addr_list.remove(addr)
            print("삭제결과")
            print(f"{target_name}은(는) 삭제되었습니다.")
        
    def editAddr(self, target_name):
        found = [addr for addr in self.addr_list if addr.name == target_name]
        if not found:
            print("수정결과")
            print(f"{target_name}은(는) 목록에 없습니다.")
            return
        for addr in found:
                new_phone_number = input("전화번호를 입력하세요: ")
                new_email = input("이메일을 입력하세요.: ")
                new_address = input("주소를 입력하세요: ")
                new_group = input("그룹(친구/가족)을 입력하세요: ")
                addr.phone_number = new_phone_number
                addr.email = new_email
                addr.address = new_address
                addr.group = new_group
        print(f"{target_name}님의 정보가 수정되었습니다.")