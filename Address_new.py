from abc import ABC, abstractmethod


class Addr(ABC):

    def __init__(self, name, phone, email, address, birthday, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
        self.group = group

    @abstractmethod
    def print_info(self):
        print(f"이름: {self.name}")
        print(f"전화번호: {self.phone}")
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}")
        print(f"생일: {self.birthday}")
        print(f"그룹(회사/거래처): {self.group}")


class CompanyAddr(Addr):

    def __init__(self, name, phone, email, address, birthday, company, department, position):
        super().__init__(name, phone, email, address, birthday, "회사")
        self.company = company
        self.department = department
        self.position = position

    def print_info(self):
        super().print_info()
        print(f"회사명: {self.company}")
        print(f"부서명: {self.department}")
        print(f"직급: {self.position}")


class CustomerAddr(Addr):

    def __init__(self, name, phone, email, address, birthday, company, item, position):
        super().__init__(name, phone, email, address, birthday, "거래처")
        self.company = company
        self.item = item
        self.position = position

    def print_info(self):
        super().print_info()
        print(f"회사명: {self.company}")
        print(f"품목이름: {self.item}")
        print(f"직급: {self.position}")