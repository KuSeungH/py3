# quiz2.py

# 1) 세 정수를 입력받어서 가장 작은 수를 화면에 출력하세요
n1 = int(input('첫번째 정수 입력 : '))
n2 = int(input('두번째 정수 입력 : '))
n3 = int(input('세번째 정수 입력 : '))

minValue = n1
if minValue > n2:
    minValue = n2
if minValue > n3:
    minValue = n3

print(' {}, {}, {} 중 최솟값 : {}'.format(n1, n2, n3, minValue))

# 2) 15층 건물에 엘리베이터가 3개 있다
# 사용자가 현재층을 입력하면 
# 3개의 엘리베이터 중 가장 가까운 엘리베이터가 이동하도록 작성하세요

# A, B, C : 3, 13, 7
# 사용자 호출 : 11
# B엘리베이터가 이동합니다

import random
eleA = random.randint(1, 15)
eleB = random.randint(1, 15)
eleC = random.randint(1, 15)
print('A, B, C : {}, {}, {}'.format(eleA, eleB, eleC))

user = int(input('사용자 호출 위치 : '))
distA = abs(user - eleA)    # 절대값을 만드는 함수 = abs(n)
distB = abs(user - eleB)
distC= abs(user - eleC)
print(distA, distB, distC)  # 엘리베이터와 사용자 사이의 거리(절대값)

minDist = distA
if distB < minDist: # 이전과 상관없이 항상 체크
    minDist = distB
if distC < distC:
    minDist = distC

if minDist == distA:      print('A엘리베이터가 움직입니다')
elif minDist == distB:    print('B엘리베이터가 움직입니다')
else:                     print('C엘리베이터가 움직입니다')
