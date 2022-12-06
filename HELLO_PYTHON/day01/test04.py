# 로또를 생성하시오(1~45숫자 중에서 중복없이 6개 가져오기)
import random

arr = []
ran = random.randint(1,45)
print(ran)

for i in range(6):
    arr[i]=ran