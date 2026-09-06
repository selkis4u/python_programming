class BankAccount:
    # 1. 생성자 (초기화)
    def __init__(self, owner, balance=0):
        self.owner = owner  # 공개 속성 (예금주)
        self.__balance = balance  # 비공개 속성 (잔액: 외부에서 직접 수정 방지)

    # 2. 입금 기능 (메서드)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount:,}원이 입금되었습니다. 현재 잔액: {self.__balance:,}원")
        else:
            print("입금액은 0원보다 커야 합니다.")

    # 3. 출금 기능 (메서드)
    def withdraw(self, amount):
        if amount <= 0:
            print("출금액은 0원보다 커야 합니다.")
        elif amount > self.__balance:
            print("잔액이 부족합니다.")
        else:
            self.__balance -= amount
            print(f"{amount:,}원이 출금되었습니다. 현재 잔액: {self.__balance:,}원")

    # 4. 잔액 조회 기능 (게터 역할)
    def get_balance(self):
        return self.__balance

    # 계좌 생성 (철수의 통장 개설, 초기 잔액 10,000원)
acc = BankAccount("김철수", 10000)

acc.deposit(5000)  # 5,000원 입금 -> 잔액: 15,000원
acc.withdraw(3000)  # 3,000원 출금 -> 잔액: 12,000원
acc.withdraw(50000)  # 잔액 부족 처리

# 비공개 변수 보호 확인
# acc.__balance = 100000000  <- 이런 식으로 직접 조작하는 것이 통하지 않음
print(f"최종 확인 잔액: {acc.get_balance():,}원")