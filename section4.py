# 현재시간과 날짜 가져오기
from datetime import datetime

now = datetime.now()

print(now)


# 정보 추출하기
from datetime import datetime

now = datetime.now()

print(now)

current_year = now.year
current_month = now.month
current_day = now.day

print(current_year)
print(current_month)
print(current_day)


# 날짜 정보 다듬기
from datetime import datetime
now = datetime.now()

print(str(now.month)+"/"+str(now.day)+"/"+str(now.year))




# 시간 정보 다듬기
from datetime import datetime
now = datetime.now()

print(str(now.month)+"/"+str(now.day)+"/"+str(now.year))
print(str(now.hour)+":"+str(now.minute)+":"+str(now.second))



# 복습하기 마무리
from datetime import datetime
now = datetime.now()

print(str(now.month)+"/"+str(now.day)+"/"+str(now.year) + " " \
      + str(now.hour)+":"+str(now.minute)+":"+str(now.second))

