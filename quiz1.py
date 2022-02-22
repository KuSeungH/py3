# quiz1.py

# 1) 숫자를 입렵받아서 절대값을 구하는 프로그램을 작성하시오



n1 = int(input('숫자입력 :'))
also = 0
if n1 > 0:
    also = n1
else:
    also = -n1
print('{}의 절대값은 {}입니다'.format(n1,also))


# 2) 사격 시뮬레이션 프로그램을 만드는 중이다
#    유효사거리는 50m 이며, 목표와 사용자간의 거리를 입력받는다
#    사용자 위치에 따라 거리를 보정하기 위한 코멘트를  출력하세요
# 입력) 사용자의 거리를 입력하세요 : 80
# 출력) 유효사거리보다 30m 멀리 있습니다
#
# 입력) 사용자의 거리를 입력하세요 : 39
# 출력) 유효사거리보다 11m 가까이 있습니다
#
# 입력) 사용자의 거리를 입력하세요 : 50
# 출력) 유효사거리와 정확히 일치합니다
print()

user = int(input('사용자의 거리를 입력하시오 : '))
effectiveRange = 50
dist = effectiveRange - user
text = '유호사거리보다 {}m {}있습니다'

if user > effectiveRange:
    text = text.format(-dist, '멀리')
    print(text)
elif user < effectiveRange:
    text = text.format(dist, '가까이')
    print(text)
else:
    print('유호사거리와 정확히 일치합니다')

    