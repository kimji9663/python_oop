# path : /exception/except_sample.py
# module : exception.except_sample

# 파이썬에서의 예외 처리 (Exception Handling)테스트 스크립트
'''
예외 : 소스코드로 해결할 수 있는 에러
에러의 종류 :
    - 시스템 에러 : 소스코드로 해결 못하는 에러
        메모리 부족, 하드디스크(저장장치) 용량 부족, 베터리 전원 부족 등
    - 구문(문법) 에러 : 코드를 잘못 작성한 경우
        개발툴에서 자동 검사됨, 구문을 수정해서 해결
    - 런타임 에러 : 실행 시 발생하는 에러
        사용자 입력 오류 등, 코드 수정해서 해결 => 예외 처리 가능

에러 처리 방법 :
    if 조건문으로 에러 상황을 예측해서 미리 조치하는 것이 일반적 
    => 파이썬에서는 예외 상황(예측된 에러 상황)을 처리하는 별도의 구문이 있음 : 예외 처리 구문 사용 권장
'''

def test_error():
    '에러 발생 예제 테스트 함수'
    # print('test error) # SyntaxError: unterminated string literal : 직접 수정

    # 컴퓨터는 0을 나누는 연산을 할 수 없다.
    # a = 10
    # b = 0
    # c = a / b

    # 값을 선언하지 않은 변수는 사용 불가
    # 4 + new * 3

    # 존재하지 않는 값
    lst = [1, 2]
    print(lst[2]) # => RuntimeError

    # 존재하지 않는 키
    dct = {'a':100, 'b':200} 
    print(dct['c']) # => RuntimeError
# test_error end -------------------------

# 런타임 에러 중 사용자가 입력값을 잘못 입력하는 경우
def test_input_error():
    '입력 오류 관련 에러 테스트용 함수'
    # num = int(input('정수를 입력 :')) # 정수가 아닌 값을 입력시 오류 발생
    # print(num)
    # if문으로 해결할 수 없는 에러 발생 상황 => 예외 처리 구문 사용

    # 해결방법 1 : 입력 따로 조건 처리로 형변환 따로 작성
    num = input('정수를 입력 :')
    if num.isdecimal(): # 10진 정수인지 체크
        num = int(num)
        print(num, type(num))
    else:
        num = input('정수 숫자만 입력하세요. 다시 입력 :')
# test_input_error end ----------------------------

# 해결방법 2 : 예외 처리 구문 사용
'''
try:
    런타임 에러 가능성 있는 구문 또는 일반 구문
except:
    에러가 발생했을 때 실행할 구문
'''

def test_input_error2():
    try:
        num = int(input('정수를 입력 :'))
        print(num, type(num))
    except:
        print('정수 숫자만 입력하세요.')
# test_input_error2 end --------------------

# 오류 발생 시 프로그램 종료가 아닌 재 동작 시키는 방법
# 예외 처리시 except:에 pass를 사용
def except_pass():
    lst = ['3', '예외처리', 4, 2, 77, 5, 'Python']
    digit_num = []
    print(lst)

    # lst에서 숫자만 골라내서 digit_num에 기록 저장 처리함
    for idx in range(len(lst)): # len(lst): 저장 갯수 리턴 => range(갯수): 0 ~ 갯수 - 1 까지의 숫자를 생성함.
        try:
            digit_num.append(int(lst[idx]))
        except:
            pass
    # for end -----------------------
    print(digit_num) # [3, 4, 2, 77, 5]
# except_pass end -----------------------

# finaly : 예외 발생과 상관없이 실행할 구문
import math # 수학 계산 관련 함수 제공

def test_finaly():
    'finaly 구문 사용 테스트 함수'
    try:
        radius = float(input('반지름 : '))
    except:
        print('숫자만 입력해야 합니다.')
    else: # 반드시 except 사용
        print('반지름 값 : ', radius)
        print('원 면적 : ', math.pi * math.pow(radius, 2))
    finally: # 항상 맨 마지막에 작성
        print('예외 처리 구문 작성 완료')
# test_finaly end ----------------------------


# 실행 테스트
if __name__ == '__main__':
    # test_error()
    # test_input_error()
    # test_input_error2()
    # except_pass()
    test_finaly()


# 다음시간에는 함수와 모듈