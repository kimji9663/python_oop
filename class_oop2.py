# path : /class_oop2.py
# module : class_oop2

# OOP 에서의 연산자 오버로딩 (oprtator overloading)

# 오버로딩 : 클래스 안에서 이름이 같은 메소드 중복 작성(정의)
# 파이썬에서는 생성자와 메소드는 오버로딩 안됨 => 오버로딩 시 마지막에 작성한 것으로 덮어쓰기 됨
# C++, Python 에서는 값 계산에 사용되는 연산자를 객체 간의 연산으로 재정의할 수 있음
# 클래스 안에 연산자와 관련된 예약어를 사용하여, 객체 간의 연산이 가능하도록 기존 연산자에 대한 메소드를 추가할 수 있음


'''
객체와 객체의 연산, 객체와 값의 연산
객체 + 값(객체) : __add__(self, 값 또는 객체)
    return self.필드 + 값 또는 return self.필드 + other.필드

객체 - 값(객체) : __sub__(self, 값 또는 객체)
    return self.필드 - 값 또는 return self.필드 - other.필드
    
객체 * 값(객체) : __mul__(self, 값 또는 객체)
    return self.필드 * 값 또는 return self.필드 * other.필드
    
객체 / 값(객체) : __truediv__(self, 값 또는 객체)
    return self.필드 / 값 또는 return self.필드 / other.필드
    
객체 // 값(객체) : __floordiv__(self, 값 또는 객체)
    return self.필드 // 값 또는 return self.필드 // other.필드
    
객체 ** 값(객체) : __pow__(self, 값 또는 객체)
    return self.필드 ** 값
    
객체 > 값(객체) : __gt__(self, 값 또는 객체)
    return self.필드 > 값 또는 return self.필드 > other.필드
    
객체 >= 값(객체) : __ge__(self, 값 또는 객체)
    return self.필드 >= 값 또는 return self.필드 >= other.필드

객체 < 값(객체) : __lt__(self, 값 또는 객체)
    return self.필드 < 값 또는 return self.필드 < other.필드

객체 <= 값(객체) : __le__(self, 값 또는 객체)
    return self.필드 <= 값 또는 return self.필드 <= other.필드

객체 == 값(객체) : __eq__(self, 값 또는 객체)
    return self.필드 == 값 또는 return self.필드 == other.필드
    
객체 != 값(객체) : __ne__(self, 값 또는 객체)
    return self.필드 != 값 또는 return self.필드 != other.필드

시퀀스나 맵 타입에 대해서도 연산자 오버로딩이 가능

타입 변환 관련 메소드 오버로딩
__int__(self)
    return int(self.필드명)

__float__(self)
    return float(self.필드명)

__bool__(self)
    return bool(self.필드명)
'''

class OOP:
    # field: private
    __num = 0

    # constructor
    def __init__(self, num):
        self.__num = num

    # 연산자 오버로딩 메소드 추가
    def __add__(self, value):
        '+ 연산자를 메소드로 오버로딩 처리'
        return self.__num + value
    
    def __sub__(self, value):
        '- 연산자를 메소드로 오버로딩 처리'
        return self.__num - value
    
    def __mul__(self, value):
        '* 연산자를 메소드로 오버로딩 처리'
        return self.__num * value
    
    def __truediv__(self, value):
        '/ 연산자를 메소드로 오버로딩 처리'
        return self.__num / value
    
    def __floordiv__(self, value):
        '// 연산자를 메소드로 오버로딩 처리'
        return self.__num // value
    
    # gatter
    def get_num(self):
        return self.__num
# class OOP end ------------------------------


# 클래스 객체 생성
ref = OOP(100)
print('ref가 참조하는 인스턴스 안의 __num 값 : ', ref.get_num())

# 객체와 값의 연산(기본적으로는 불가)
# print('ref > 30 :', ref > 30) # __gt__메소드로 오버로딩 안하면 오류 발생

# 내부 연산 메소드로 오버로딩
print('ref + 30 :', ref + 30) # 130
print('ref - 30 :', ref - 30) # 70
print('ref * 30 :', ref * 30) # 3000
print('ref / 30 :', ref / 30) # 3.3333333333333335


# len() : 길이(저장된 값의 갯수)를 구하는 내장함수
# 리스트, 튜플, 문자열 같은 시퀸스 자료형에 주로 사용
# 연산자 오버로딩으로 추가할 수 있음
class MyNumber:
    # 필드가 없는 경우, 자동으로 필드를 추가해 줌
    def __init__(self, value):
        self.value = value # 실행 시 value라는 필드 추가

    def __len__(self):
        return self.value
# class MyNumber end ------------------    

ref = MyNumber(5)
print('len() :', len(ref)) # 5


# in 연산자 오버로딩도 가능함
class MyBox:
    def __init__(self, items):
        self.items = items

    def __len__(self): # len()
        return len(self.items)
    
    def __contains__(self, item): # in 연산자
        return item in self.items
# class MyBox end ---------------------


box = MyBox({1, 2, 3})
print(len(box)) # 3
print(2 in box) # True
print(5 in box) # False


# 인덱싱 : [index] 연산자 오버로딩
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index): # [index] 인덱싱 연산자 오버로딩
        return self.data[index]
    
    def __str__(self): # 자바의 toString() 같은 메소드
        return str(self.data)
# class MyList -------------------------

mylist = MyList([10, 20, 30])

print(len(mylist)) # 3
print(mylist[0]) # 10  __getitem__이 작동
print(mylist) # [10, 20, 30]  __str__ 실행 # 문자열로 출력된건지 확인 필요