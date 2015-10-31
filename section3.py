# -*- coding: utf-8 -*-

# 세 번째 줄에 변수 brain을 생성하세요!

brian = "언제나 삶의 긍정적인 면을 살피세요!"


# 각 줄마다 하나씩, 변수들을 생성하고 값을 지정하세요!

caesar = "Graham"
praline = "John"
viking = "Teresa"

# 변수들은 이 줄 위에 작성되어야 합니다.

print(caesar)
print(praline)
print(viking)



# 아래의 문자열에 문제가 있습니다. 백슬래쉬를 이용하여 고쳐보세요!
# 'Help! Help! I'm being repressed!'
'Help! Help! I\'m being repressed!'
"Help! Help! I'm being repressed!"


# 오프셋으로 접근하기
"""
문자열 "PYTHON"은 여섯개의 문자를 가지고 있고,
아래와 같이 0부터 5까지 숫자가 매겨져 있습니다:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

따라서 여러분이 "Y"를 원한다면, 다음과 같이 작성하면 됩니다:
"PYTHON"[1] (언제나 순서는 0부터 세기 시작합니다!)
"""
fifth_letter = "MONTY"[4]

print(fifth_letter)



# len()
parrot = "Norwegian Blue"
print(len(parrot))



# lower()
parrot = "Norwegian Blue"

print(parrot.lower())



# upper()
parrot = "norwegian blue"

print(parrot.upper())



# str()
"""네 번째 줄에서 변수를 선언하고 값을 지정하세요.
그런 다음 다섯 번째 줄에서 메소드를 호출하세요!"""

pi = 3.14
print(str(pi))



# 점 표기법
ministry = "The Ministry of Silly Walks"

print(len(ministry))
print(ministry.upper())


# 문자열 리터럴 출력
"""네 번째 줄에서 파이썬에게 "Monty Python"을
console에 출력하라고 전하세요!"""

print("Monty Python")


# 변수 출력하기
"""다섯 번째 줄에 변수 the_machine_goes
를 선언하고 문자열 "Ping!"을 값으로 지정하세요.
그런 다음, 여섯 번째 줄에서 변수를 출력하세요!"""

the_machine_goes = "Ping!"
print(the_machine_goes)



# 문자열 연결
# 세 번째 줄에서 "Spam and eggs"의 연결된 문자열을 출력하세요!

print("Spam "+"and "+"eggs")

print(" ".join(["Spam", "and", "eggs"]))



# 명확한 문자열 변환
# 세 번째 줄에서 숫자 3.14를 문자열로 바꿔보세요!

print("The value of pi is around " + str(3.14))



# %를 이용한 문자열 포맷팅
name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))



# 복습하기
# 아래의 세 번째 줄부터 코드를 작성하세요!

my_string = "test"
print(len(my_string))
print(my_string.upper())