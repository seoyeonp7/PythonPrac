# 로또를 생성하시오(1~45숫자 중에서 중복없이 6개 가져오기)
from random import random

arr45 = list(range(1,46))
for i in range(1000):
    rnd = int(random()*45)
    emp = arr45[rnd]
    arr45[rnd]=arr45[0]
    arr45[0]=emp

for i in range(6):
    print(arr45[i],end=' ')

# print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])

    