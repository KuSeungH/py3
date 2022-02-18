#ex03.py
# 사용자에게 입력하기

'''
    입력 => 처리 => 출력
           CPU
           RAM
           HDD
'''

age = (input('나이를 입력하세요 : '))
age = int(age)  # 입력받은 age는 문자열인데 정수형으로 바꿔서 저장
print(age)
print(type(age))
#input() 로 입력받으면 문자열 형태가 된다
# 문자열을 다른 자료형으로 변경하려면 int(age) 와 같이
# 자료형 뒤에 괄호를 열고 변경을 원하는 변수를 넣어준다

age2 = int(input('나이입력'))
adult = (age2 >= 20) and '성인' or '미성년자'
print('당신은 {}살이고, {}입니다'.format(age2, adult))