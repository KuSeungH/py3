# ex03.py
# while : 조건이 참인동안 계속해서 반복 수행하는 제어문

num = 10

if num < 20:
    num += 1
    print('if)', num)

while num < 20:
    num += 1
    print('while)', num)

# 1) 지정한 횟수만큼 문자열을 출력하기
hello = 'hello world!!'
cnt = 0
while cnt < 5:
    print(hello, cnt)
    cnt += 1
# 2) 원하는 범위의 숫자만 입력받기
while True:
    score = int(input('점수 입력 (0 ~ 100) : '))
    if 0 <= score and score <= 100:
        break      # 반복문을 탈출
    print('다시 입력하세요!!')

print('입력받은 점수 : ', score)