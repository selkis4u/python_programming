class Addr:

    def __init__(self, name, phone_num, email, address, group):
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.address = address
        self.group = group

    def print_info(self):
        print(f"이름 : {self.name}")
        print(f"전화번호 : {self.phone_num}")
        print(f"이메일 : {self.email}")
        print(f"주소 : {self.address}")
        print(f"그룹(친구/가족) : {self.group}")      