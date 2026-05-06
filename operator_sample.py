# path : /operator_sample.py
# module : operator_sample

# 연산자(operator) : 값 계산에 사용되는 기호

'''
[종류(우선순위)로 구분]
최우선 연산자(1) : '()', '.':직접접근연산자, '[]':배열과 인덱싱
단항 연산자(2) : '+':양수부호 +1*값, '-':음수부호 -1*값, '++':1증가, '--':1감소, '!':논리부정연산자, '~':tield 비트반전
이항 연산자[값 연산자 값]
    - 산술 연산자(3) : '*', '/':몫이 정수형, '//':몫이 실수형, '%':mod 나머지, '**':제곱
    - 산술 연산자(4) : '+':더하기, '-':빼기
    - 쉬프트 연산자(5) : '<<', '>>':비트값 자리 이동 연산자
    - 관계(비교) 연산자(6) : '>':초과, '<':미만, '>=':이상, '<=':이하
    - 관계(비교) 연산자(7) : '==':같다, '!=':같지않다
      관계(비교) 연산자[값 비교연산자 비교값] => 결과값이 논리값임 True or False
    - 논리 연산자(8) : 'and':True and True => True, 한개라도 False이면 False
    - 논리 연산자(9) : 'xor':논리값이 다르면 True, 같으면 False
    - 논리 연산자(10) : 'or':둘 중 하나만 True이면 True
삼항 연산자[조건표현식 ? 참 : 거짓]
대입 연산자 : '=', '-=', '-=', '*=', '/=', '//=', '%=', '**='
나열 연산자 : ','
'''

# bool 자료형 확인
def func_bool():
    flag = True
    print('flag :', flag, type(flag))

    # 파이썬에서는 대소문자 구분함
    # bool()함수 : 값의 논리 상태를 확인할 때 사용함
    print('문자가 있는 문자열 : ', bool('abcd')) # True
    print('빈 문자열 : ', bool('')) # false

    # 값이 저장되어 있는지, 비어 있는지 확인하는 용도로 사용함
    print('result : ', bool({'a':10, 'b':20})) # 값이 있으므로 True
    print('result : ', bool({})) # 값이 없으므로 False

    # 0을 제외한 모든 값은 True
    print('0을 제외한 모든 값 :', bool(12)) # True
    print('0 :', bool(0)) # False

# 비교(관계) 연산자 확인
# 값 연산자 비교값 => True | False
def op_compare():
    print('1 == 1 :', 1 == 1) # True
    print('1 == 2 :', 1 == 2) # False

    print('1 > 0 :', 1 > 0) # True
    print('1 < 2 :', 1 < 2) # True

    print('1 >= 1 :', 1 >= 1) # True
    print('1 != 0 :', 1 != 0) # True

# 논리 연산자 : 논리값(True, False)을 계산에 사용하는 연산자
# and, or, not
def op_logical():
    a = 1
    b = 2
    print(a > 0 and b > 1) # True and True => True
    print(a > 0 or b != 1) # True or False => False

    # and 연산자의 특징
    # 앞 and 뒤 : 앞이 False 이면 뒤를 실행하지 않음, 앞이 True 이면 뒤를 실행함
    # 위 특징을 이용한 짧은 조건문(모든 스크립트에서 사용함)
    print('a' and 'b') # 'a'가 True이면 'b'를 실행함
    print('' and 'b') # 'a'가 False이면 '' 출력

    # or 연산자의 특징
    # 앞 or 뒤 : 앞이 False이면 뒤를 실행함, 앞이 True 이면 뒤를 실행하지 않음
    print('a' or 'b') # 'a'가 True이면 'a'를 출력
    

if __name__ == '__main__':
    # func_bool()
    # op_compare()
    op_logical()

# 파이썬은 기본적으로 배열을 취급하지 않기 때문에 numpy를 별도로 설치해야 한다.