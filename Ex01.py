# ex01.py
# 연산자 

# 파이썬에서 여러 데이터를  묶어서 처리할 때는 리스트를 사용
list1 = [1,2,3,4,5]

print('3이 list1에 포함되어 있다 :', 3 in list1)
print('6이 list1에 포함되어 있다 :', 6 in list1)
print('3이 list1에 포함되어 있다 :', 3 not in list1)
print('6이 list1에 포함되어 있다 :', 6 not in list1)
print()

list2 = ['용돈', '꽃', '넥타이', '음식', '옷']
wish = input('받고싶은 품목을 입력 : ')
print(wish in list2 and '지금 있습니다' or '준비되지 않았습니다')
print()

'''
        **              지수곱하기
        ~, +, -         비트 'NOT', 부호결정(양수, 음수)
        *, /, %, //     곱하기 및 나누기
        +, -            덧셈 뺼셈
        >>, <<          비트 시프트
        $               비트 AND
        ^, ㅣ            비트 OR, 논리 OR
        <=, <, >, >=    비교 연산자
        =, +=, *=       대입 연산자
        is, not in      식별 연산자
        in, not in      멤버 연산자(맴버 인지 아닌지 확인)
        not, or, and    논리 연산자  
'''

