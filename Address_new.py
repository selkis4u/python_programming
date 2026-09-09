class Addr:

       
    def __init__ (self, name, phone_number, email, address, group, birthday):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.group = group
        self.birthday = birthday
        

    def print_info(self):
        
        print(f"이름 : {self.name}")
        print(f"전화번호 : {self.phone_number}")
        print(f"이메일 : {self.email}")
        print(f"주소 : {self.address}")
        print(f"그룹(회사/거래처): {self.group}")
        print(f"생일 : {self.birthday}")

    
class CompanyAddr(Addr):

    def __init__(self, name, phone_number, email, address, group, birthday, company_name, department, level):
        super().__init__(name, phone_number, email, address, group, birthday)
        self.company_name = company_name
        self.department = department
        self.level = level

    def print_info(self):
        super().print_info()
        print(f"회사이름 : {self.company_name}")
        print(f"부서이름 : {self.department}")
        print(f"직급 : {self.level}")


class CustomerAddr(Addr):
    def __init__(self, name, phone_number, email, address, group, birthday, customer_name, item_name, level):
        super().__init__(name, phone_number, email, address, group, birthday)
        self.customer_name = customer_name
        self.item_name = item_name
        self.level = level

    def print_info(self):
        super().print_info()
        print(f"거래처 이름: {self.customer_name}")
        print(f"품목이름: {self.item_name}")
        print(f"직급: {self.level}")