class Addr:


    def __init__(self, name, phone_number, email, address, group):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.group = group
        
    def __str__(self):
        return (
        f"이름 : {self.name}\n"
        f"전화번호 : {self.phone_number}\n"
        f"이메일 : {self.email}\n"
        f"주소 : {self.address}\n"
        f"그룹(친구/가족) : {self.group}"
    )