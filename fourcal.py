#-*- coding: utf-8 -*-
"""
ch05-1 사칙연산 클래스 만들기 (슬라이드 18-32)
FourCal 클래스를 슬라이드 순서대로 단계별 구현
"""

#----------------------------------------------------
#[1단계] p.19 클래스 구조만 만들기 - pass
#----------------------------------------------------
class FourCalStep1:
    pass


#----------------------------------------------------
#[2단계] p.21 setdata로 연산할 두 숫자 저장하기
#self .first : 인스턴스 변수 (객체에 계속 남음)
#first       : 로컬 변수 (메서드가 끝나면 사라짐)
#----------------------------------------------------
class FourCalStep2:
    def setdata(self, first, second):
        self.first = first
        self.second = second

#----------------------------------------------------
#[3단계] p.27~28 add/ sub/ mul / div 메서드 추가
# 네 메서드 모두 매개변수가 self 하나뿐~
# 필요한 값이 이미 객체 안에 저장되어 있기 때문
#----------------------------------------------------
class FourCalStep3:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


#----------------------------------------------------
#[4단계.최종] p.30~32 생성자(__init__) 방식
# 객체를 만들 때 값을 반드시 넣도록 강제 ->
# setdata를 빠뜨려 생기는 AttributeError를 원천 차단
#----------------------------------------------------
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


#----------------------------------------------------
# 실행 예제
#----------------------------------------------------
if __name__ == "__main__":

    # [1단계] 빈 클래스도 객체를 만들 수 있다. (p.19)
    a = FourCalStep1()
    print("1단계 type(a) :", type(a))

    # [2단계] setdata로 값 저장 (p.21, p.25~26)
    a = FourCalStep2()
    b = FourCalStep2()
    a.setdata(4, 2)
    b.setdata(3, 7)
    print("2단계 a.first, b.first :", a.first, b.first)
    print("2단계 id(a) != b(id) :", id(a) != id(b))
    print("2단계 id(a) != b(id) :", id(a), id(b))

    # [3단계] 사칙 연산 (p.27~28)
    a = FourCalStep3()
    b = FourCalStep3()
    a.setdata(4, 2)
    b.setdata(3, 8)
    print("3단계 a:", a.add(), a.sub(), a.mul(), a.div())
    print("3단계 b:", b.add(), b.sub(), b.mul(), b.div())

    # [3단계] setdata 없이 add 호출하면 AttributeError (p.29)
    try:
        FourCalStep3().add()
    except AttributeError as e:
        print("3단계 오류 :", e)

    # [4단계] 생성자 방식 - 한줄로 객체 생성 + 값 전달(p.31 ~32)
    a = FourCal(4, 2)
    b = FourCal(3, 8)
    print("4단계 a:", a.add(), a.sub(), a.mul(), a.div())
    print("4단계 b:", b.add(), b.sub(), b.mul(), b.div())

    # [4단계] 값 없이 만들면 객체 생성 시점에 바로 TypeError (p.32)
    try:
        FourCal()
    except TypeError as e:
        print("4단계 오류: ", e)

    # 0으로 나누기
    try:
        FourCal(4,0).div()
    except ZeroDivisionError as e:
        print("나누기 오류 :", e)