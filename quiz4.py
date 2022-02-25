# quiz4.py

# 1) 1부터 입력받을 수 사이의 3의 배수를 한줄에 출력하세요
from re import I, T
from traceback import format_tb


num1 = int(input('정수 압력 : '))
for i in range(1, num1 + 1):
    if i % 3 == 0:
        print(i, end=' ')
print()


# 2) 1부터 100 사이의 홀수의 합과 짝수의 합을 각각 출력하세요
oddSum, evenSum = 0, 0
for i in range(1, 101):
    if i % 2 == 0:
     evenSum += i
    else:
        oddSum += i
print('홀수의 합 : {}, 짝수의 합 : {}'.format(oddSum, evenSum))


# 3) 0 ~ 100 사이의 점수를 5회 입력받아서 가장 작은 값만 화면에 출력
num3 = 0
minValue = 101 # 어떤 숫자를 입력하더라도 최소값이 변경될 수 있도록

for i in range(5):
    while True:
        num3 = int(input('점수 입력 (0 ~100) : ' ))
        if 0 <= num3 and num3 <= 100:
            break
        print('점수를 범위안에서 입력해주세요 !! \n')

    if minValue > num3:
        minValue = num3
print('입력한 값 중 최소값은 {}'.format(minValue))



# 4) 2에서 9 사이의 정수만 입력받아서 해당 숫자의 구구단을 출력하기

dan = 0
while True:
    dan = int(input('구구단 단수를 입력 (2~9): '))
    if 2 <= dan and dan <= 9:
        break
    print('2에서 9사이를 입력하세요 !!')

for i in range(1, 10):
    print('{} x {} = {}'.format(dan, i, dan * i))

# for i in range(st, ed, p1)       파이썬
# for(int i = st; i= ed; i += p1)  c, c++, Java