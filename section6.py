# 입력값!
original = input("what is your name?")


# 직접 점검하기
original = input("what is your name?")

if len(original) != 0:
    print(original)

else:
    print("empty")


# 조금 더 점검하기
original = input("what is your name?")

if len(original) != 0 and original.isalpha():
    print(original)

else:
    print("empty")

# 단어분석
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print(original)
else:
    print('empty')



# 모음으로 시작하는 단어 번역
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first in {'a','i','e','o','u'}:
        new_word = word+pyg
        print(new_word)
    else:
        strlen = len(word)
        new_word = word[strlen::-1]  # 반대로 출력하기.. 수정
        print(new_word)
else:
    print('empty')

