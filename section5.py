# 자세히 비교하기
# 아래의 각 변수들에 적합한 True 또는 False 값을 할당하세요!
bool_one = 17 <118 % 100

bool_two = 100 == 33 * 3 + 1

bool_three = 19 <= 2**4

bool_four = -22 >= -18

bool_five = 99 != 98 + 1



# 더더 자세히 비교하기
# 아래의 각 변수들에 적합한 True 또는 False 값을 할당하세요!

bool_one = 20 + -10 * 2 > 10 % 3 % 2

bool_two = (10+17)**2 == 3**6

bool_three = 1**2**3 <= -(-(-1))

bool_four = 40 / 20* 4 >= -4 **2 # 파이썬은 먼저 제곱한후 음수처리 한다.

bool_five = 100**0.5 != 6+4


# 반대로 비교하기
# 아래의 각 변수들이 알맞은 불린값을 갖도록 비교문을 작성하세요!

# 변수의 값이 참이 되도록 만드세요!
bool_one = "test" == "test"

# 변수의 값이 거짓이 되도록 만드세요!
bool_two = 1+3 > 71

# 변수의 값이 참이 되도록 만드세요!
bool_three = 40**1 != 39**2

# 변수의 값이 거짓이 되도록 만드세요!
bool_four = 67%3 != 4%3

# 변수의 값이 참이 되도록 만드세요!
bool_five = 30 + 40 <= 70


# 같거나(AND), 또는(OR) 반대(NOT)이거나
"""
     불린 연산자(Boolean Operators)
-----------------------------------------------
True 그리고(and) True의 결과는 True
True 그리고(and) False의 결과는 False
False 그리고(and) True의 결과는 False
False 그리고(and) False의 결과는 False

True 또는(or) True의 결과는 True
True 또는(or) False의 결과는 True
False 또는(or) True의 결과는 True
False 또는(or) False의 결과는 False

True 부정(not)의 결과는 False
False 부정(not)의 결과는 True

"""



# AND 연산자
bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300/10/10 and False

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True



# OR 연산자
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or Flase

bool_three = 100**0.5 >= 50 or False

bool_four =  True or True

bool_five = 1**100 == 100**1 or 3*2*1 != 3+2+1



# NOT 연산자
bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 %3 <= 10%2

bool_four =  not 3**2 + 4**2 != 5**2

bool_five = not not False


# 복습
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)


# 반대로 보습
# 아래의 각 변수들이 알맞은 불린값을 갖도록 수식을 작성하세요!

# 변수의 값이 거짓이 되도록 만드세요!
bool_one = "test" == "test" and "test" != "test"

# 변수의 값이 참이 되도록 만드세요!
bool_two = False or True

# 변수의 값이 거짓이 되도록 만드세요!
bool_three = False or False

# 변수의 값이 참이 되도록 만드세요!
bool_four = True or False

# 변수의 값이 참이 되도록 만드세요!
bool_five = True and True




# 조건 명령문의 문법
# 아래의 print 명령문이 console에 출력될까요?
# 그럴거 같다면 변수 response에 'Y'를, 그렇지 않다면 'N'을 값으로 지정하세요.
response = 'Y'

answer = "Left"
if answer == "Left":
    print("이런, 방을 잘못 들어왔습니다!")


# if문의 문법
def using_control_once():
    if 1 :
        return "Success #1"

def using_control_again():
    if 1 :
        return "Success #2"

print(using_control_once())
print(using_control_again())


# if / else 문
answer = "이 정돈 그냥 긁힌거지!"

def black_knight():
    if answer == "이 정돈 그냥 긁힌거지!":
        return True
    else:
        return False       # False 값을 반환하도록 만드세요

def french_soldier():
    if answer == "저리 꺼져, 그렇지 않으면 또 다시 본떼를 보여주마!":
        return True
    else:
        return False       # False 값을 반환하도록 만드세요



# if/ elif문
def greater_less_equal_5(answer):
    if answer > 5 :
        return 1
    elif answer < 5 :
        return -1
    else:
        return 0

print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))


# 복습하기
def the_flying_circus(num1,num2):
    # 여기서 부터 코딩을 시작하세요!
    if num1 > 5 and num2 > 5:
        return 1

    elif num1 < 5 and num2 < 5:
        return -1

    else:
        return 0


print(the_flying_circus(5,6))
print(the_flying_circus(6,6))
print(the_flying_circus(1,1))