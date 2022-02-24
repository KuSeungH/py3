# quiz3.py
# 은행에 돈을 입금한다 
# 첫날에는 10원을 입금하고
# 둘째날에는 전날의 2배인 20원을 입금한다
# 셋쨰날에는 전날의 2배인 40원을 입금한다
# 이런 규칙으로 30일간 입금을 하면 은행 계좌의 잔고는 얼마인가?
# 천단위 구분기호를 적용하여 결과를 출력하세요

money = 10
day = 1
bank = 0

while day <= 30:    # 1 ~ 30
    bank += money
     # print('{}일, {:,d}입금, 잔고 : {:,d}'.format(day, money, bank))
    money *= 2
    day += 1
print('잔고 : {:,d}원'.format(bank))