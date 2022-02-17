# ex02.py
# 제어문 (control statement)
# if ~ elif ~ else
# while
# for

# 파이썬은 들여쓰기를 제대로 지키지 않으면 실행할 수 없다
# 1) C언어와 달리 중괄호를 이용하여 블럭을 나누지 않는다
# 2) 중괄호 대신 들여쓰기로 처리한다
# 3) 공백(space), 탭(tab) 둘다 가능하지만 공백수가 일치해야 한다

if True:
    print('True')

else:
    print('False')


# 파이썬 IF는 숫자도 받고, 논리값도 받는다
# 숫자는 0이 아니면 True로 처리
print()
num1 = 50
if num1:
    print(True)
else:
    print(False)

if num1 > 10:
    print('num1은 10보다 크다')
elif num1 < 10:
    print('num1은 10보다 작다')
else:
    print('num1 과 10이 같다')
print()

# 정수를 입력받아서, 양수와 음수를 판별하세요 (if ~ else)
num = int(input('정수입력 : '))
if num > 0:                             # 조건 판별
    print('{} : 양수'.format(num))
elif num == 0:                          # if가  False이면 판별
    print('0은 음수도 양수도 아닙니다')
else:   # 이전 모든 조건이 False라면 else이하를 실행
    print('{} : 음수'.format(num))


