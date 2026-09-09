from Address import Addr


class SmartPhone:

    def __init__(self):
        self.addr_list = []
        self.MAX_SIZE = 12

    def inputAddData(self):
        name = input("이름을 입력하세요: ").strip()
        phone_number = input("전화번호를 입력하세요: ").strip()
        email = input("이메일을 입력하세요: ").strip()
        address = input("주소를 입력하세요: ").strip()
        group = input("그룹(친구/가족)을 입력하세요: ").strip()
        return Addr(name, phone_number, email, address, group)

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