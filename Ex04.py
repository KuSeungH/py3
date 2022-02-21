# Ex04.py
# for : 지정한 횟수에 의해  반복하는 제어문

# for(int i = 0; i < 5; i++) {
#   print("%d\n", i):
# }

from re import I
from time import sleep


for i in range(5):          # range(end), 0부터 end보다 작을때 까지 반복
    print(i, end=' ')
print()

for i in range(0, 5):       # range(start, end), start부터 end보다 작을때 까지
    print(i, end=' ')
print()

for i in range(0, 5, 1):   # range(start, end, plus),
    print(i, end=' ')      # start 부터 end보다 작을때 까지 plus씩 증가시킴
print()

# 1부터 10까지의 합계를 구하고 싶다면
total = 0
for i in range(1, 11):
    total += i
print('1부터 10까지의 합 :', total)

# 한칸씩 증가하는 반복되는 문자열을 만들고 싶다면

from os import system
from time import sleep

ch = '😁'
for i in range(20): # 콘솔창 출력된 내용을 지운다
    system('cls')   # 글자를 갯수만큼 출력한다
    print(ch * i)   # 컴퓨터에게 0.2초만큼 일시정지 한다
    sleep(0.2)
     

ch = '🐶'
system('clear')
print(ch * 1)
sleep(0.2)

system('clear')
print(ch * 2)
sleep(0.2)

system('clear')
print(ch * 3)
sleep(0.2)

system('clear')

second = int(input('몇 초 카운트할까요 :'))
for i in range(second, -1, -1):
    print('{}초 남았습니다'.format(i))
    sleep(1)
print('종료')

for i in range(0, 10, 1):
    num = 2 ** i
    print(i, end=' ')
print()
