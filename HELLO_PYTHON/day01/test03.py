# 홀/짝을 넣으세요 홀
# 나:홀
# 컴:짝
# 결과:졌음
import random

user = input("홀/짝을 넣으세요")
com=""
result = ""
rnd = random.random()
if rnd>0.5:
    com = "짝"
else:
    com = "홀"
if user == com:
    result="이김"
else:
    result="졌음"
    
print("나:"+user)
print("컴:"+com)
print("결과 : " + result)




