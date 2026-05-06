# path : /class_oop.py
# module : class_oop

# 파이썬에서 객체 지향 프로그래밍(oop) 적용
'''
객체 지향 프로그래밍에서는 클래스 멤버 구성이 중요함
field(멤버 변수), method(멤버 함수), constructor(생성자), distructor(소멸자) *필수는 아님
- oop에서 사용되는 기술(3대 특징)도 적용해야 함
  encapsulation(캡슐화),  inhritance(상속), polymorphism(다형성)

'''


# OOP 적용 기술 1 : 캡슐화
# 캡슐화 : 데이터 보호 목적. 필드에 접근 제한을 설정함
# 필드에 접근 제한자(access modifier)를 사용함
# private(비공개: 캡슐화), public(공개),  protected(상속시 후손에게만 공개)

# 파이썬에서는 접근 제한자 없음(제공 안 함)
# 파이썬에서는 기본적으로 클래스 안의 모든 멤버는 public임
# 클래스를 자료형(type)으로 만든 변수 == 레퍼런스 변수라고 함 : 클리스로 만들어진 긱체의 주소를 가짐
# 레퍼런스.필드명, 클래스명.필드명
# 레퍼런스.메소드명, 클래스명.메소드명()

# private : 클래스 밖에서 사용 못 함, 클래스 안에서만 사용(접근)할 수 있음
# 파이썬에서 클래스 멤버를 비공개(private)처리 하려면,
# 필드명이나 메소드명 이름 앞에 '_'(underscore)를 두개 붙이면 됨

class PClass:
    # field (private)
    __num = 10

    # constructor 추가 : 매개 변수 있는 생성자를 작성함
    # def __init__(self): # 매개변수 없는 기본 생성자
    #     self.__num = 0

    def __init__(self, num): # 매개변수 있는 생성자 1개만 만들 수 있음
        self.__num = num

    # method (public)
    def set_num(self, num): # num 값을 수정
        self.__num = num


    def get_num(self): # num 값을 출력
        return self.__num 
# PClass end --------------------------------

# 클래스 멤버 사용 : 레퍼런스 변수 = 클래스명() 또는 레퍼런스 = 클래스명(전달값)
# pref = PClass() # 매개번수 없는 기본 생성자 자동 실행됨. 메모리에 객체 공간 할당하고 주소를 리턴함
# print('pref가 가진 주소 : ',  id(pref))
# print('인스턴스 안의 __num 값 : ', pref.get_num())

# 클래스 밖에서 필드 접근 확인
# print('인스턴스 안의 __num 값 : ', pref.__num) # private 이기 때문에 접근할 수 없어서 오류 발생


# 생성자 (constructor)
# 객체 인스턴스가 메모리에 할당될 때, 필드값 초기화가 목적인 함수
# 생성자가 없으면, 내부에서 기본생성자를(매개변수 없는) 자동 작동함
# 기본 생성자는 직접 작성할 필요 없다.
# 생성자를 직접 작성 한다면, __init__으로 정의해야 함
# 파이썬에서는 생성자는 오버로딩(overloading)할 수 없음 : 생성자는 1개
# 주로 매개변수 있는 생성자를 추가 작성함
pref2 = PClass(20)
print('pref2가 참조하는 인스턴스 안의 필드 값 확인 : ', pref2.get_num())

# destructor (소멸자 함수)
# 객체 인스턴스가 메모리에서 제거(소멸)될 때 자동 실행되는 함수임
# 클래스 안에 직접 작성한다면, __del__로 정의해야 함
# 해당 객체 관련 메모리나 자원들의 공유 설정, 점유 설정 등을 해제할 때
'''
class 클래스명:
    def __del__(self):
        해당 클래스 객체가 소멸될 때 같이 제거 또는 해제할 내용에 대한 코드 작성
'''

class Var:
    # field: private
    __number = 100

    # constructor
    def __init__(self, n):
        print('__init__ self가 전달받은 주소 확인 : ', id(self))
        self.__number = n

    # destructor
    def __del__(self):
        print('인스턴스 제거 시 자동 작동됨 : ', id(self))

    # method : getter and setter
    def set_number(self, n):  # 생성자와 사용 시점이 다름
        print('set_number self가 전달받은 주소 확인 : ', id(self))
        self.__number = n

    def get_number(self):
        print('get_number self가 전달받은 주소 확인 : ', id(self))
        return self.__number
# Var end -------------------------------------

# 클래스 객체 생성 : 생성자가 자동 실행됨
v1 = Var(77) # 추가된 매개변수가 할당됨
v2 = Var(99)

print( 'v1 : ', v1.get_number(), id(v1))
print( 'v2 : ', v2.get_number(), id(v2))

# 소멸자는 객체 v1동작 시 실행되고, 객체 v2동작 시 또 실행된다.
# v1 실행 시 get_number 함수방이 할당된다. 함수방을 만들면서 self 변수방도 만든다.
# 레퍼런스가 가진 주소가 self에 자동 전달된다.(self를 반드시 써야하는 이유)
# 함수가 실행되고 리턴되면 __del__소멸자가 작동되고 함수방이 삭제된다.


# 필드값 변경 : setter 사용
v1.set_number(123)
print( 'v1 : ', v1.get_number(), id(v1))
# v2.set_number(int(input('v2가 참조하는 객체의 필드 값을 변경하세요 :')))
# print( 'v2 : ', v2.get_number(), id(v2))

# 보통 실행 시 만들어지는 함수방은 동적 메모리에 만들어진다.
# but 여러 객체들이 공유하는 자원인 경우, 정적 메모리에 만들어야 하는 경우가 있다.
# 동적 메모리와 정적 메모리 사이에는 주소 참조를 쓸 수 없다. (self 사용 불가)


# 정적 메소드 (statc method) ------------------
# 프로그램 실행 시 정적 메모리(static)에 따로 기록되는 메소드를 말함
# 메소드 작성 시 메소드 이름 위에 장식자(decorator == 어노테이션 : annotation)
# #staticmethod
# self 가 없는 메소드임 => 메소드 사용 : 클래스명.메소드명()

class C:
    def ham(self, x, y):
        print('instance method : ',  x, y)

class D:
    @staticmethod # 데코레이터를 붙여주면 정적 메모리에 할당됨
    def spam(x, y): # 정적메모리에 로딩됨. self 매개변수 없음
        print('static or class method : ', x, y)

# static method는 사용 시 객체 레퍼런스(인스턴스의 주소)없이 실행함 => self가 없음
# 클래스명.메소드명(전달값)
D.spam(100, 200)

# static method를 instance method처럼 사용해도 됨
dref = D() # 기본 생성자 작동됨
dref.spam(300, 400)

# instance method는 반드시 self를 전달 받아야 함, static method처럼 사용할 수 없음
# C.ham(11, 22) # 매개변수가 3개(self, x, y)인데 2개만 전달해서 오류 발생
# 해결방법 : self에게 직접 주소 전달하면 됨
cref = C()
cref.ham(10, 20) # cref가 가진 주소를 self 매개변수에게 자동 전달
C.ham(cref, 77, 88) # cref가 가진 주소를 self 매개변수에게 직접 전달
print(id(cref), cref)