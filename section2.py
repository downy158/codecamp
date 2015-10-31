# 세 번째 줄에 변수 variable의 값으로 44.50을 지정하세요!
#네 번째 줄에 tax를 지정하세요.6.75%
#  다섯 번째 줄에 변수 tip을 생성하세요.
# Reassign meal on line 7!


meal = 44.50
tax = 0.0675
tip = 15.0 / 100

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)