# path : /class_sample.py
# module : class_sample.py

# 파이썬에서 클래스 만들어 사용하기

# 파이썬은 객체지향 스크립트 언어임 : 클래스 만들어 작동
# 절차지향 프로그래밍도 가능함 : 작성된 순서대로 작동
# 파이썬은 하이브리드 프로그래밍 언어이다.

# 파이썬에서 클래스 만들기
'''
class 클래스명:
    멤버변수 = 초기값

    def 멤버함수명(self, 매개변수, 매개변수=기본값, *매개변수)
        필드에 대한 값 처리 코드 작성
        self.멤버변수 = 변경할 값 | 계산식 처리
        return self.필드명 또는 return 결과값

- 매개변수 self: 자바, C++, C#의 this와 같음
'''
# 클래스 이름은 첫글자 대문자 권장(Naming Rule, 자바스크립트와 같음)
# *매개변수 : 가변 매개변수(변수를 여러개 받음)

class SClass:
    pass # 멤버가 없는 빈 클래스
# 비어있는 클래스도 실행 시 namespace가 할당됨 => 이름만 있어도 메모리 공간이 할당됨

# 클래스 사용 : 객체(인스턴스) 생성 => 메모리에 클래스에 대한 객체 공간 할당
ref1 = SClass()
ref2 = SClass()
# 이렇게 생성하면 ref1, ref2가 각각의 주소를 가지게 된다.

print('ref1 : ', ref1)
print('ref2 : ', ref2)

# 파이썬은 실행할 때(동적으로) 멤버변수(필드)를 추가할 수 있음
ref1.score = 100 # ref1이 참조하는 인스턴스 안에 기존에 없던 score라는 필드를 추가하고 100을 기록 저장함
print('ref1이 참조하는 객체 안의 score 필드값 : ', ref1.score)
# print('ref2이 참조하는 객체 안의 score 필드값 : ', ref2.score) # ref2가 참조하는 인스턴스에는 score가 없으므로 에러 발생


