# 가위 바위 보를 넣으시오 가위
# 나:가위
# 컴:가위
# 결과:비김
import random

user = input("가위/바위/보를 넣으시오")
com=""
result = ""
rnd = random.random()

if rnd>0.66:
    com = "가위"
elif rnd>0.33:
    com = "바위"
else:
    com="보"
    
# if user == com:
#     result="비김"
# elif (user=="가위" and com=="보") or (user=="바위" and com=="가위") or (user=="보" and com=="바위") :
#     result="user win!"
# else:
#     result="computer win!"
    
    
if com =="가위" and user=="가위": result="비김"
if com =="가위" and user=="바위": result="이김"
if com =="가위" and user=="보": result="짐"

if com =="바위" and user=="가위": result="짐"
if com =="바위" and user=="바위": result="비김"
if com =="바위" and user=="보": result="이김"

if com =="보" and user=="가위": result="이김"
if com =="보" and user=="바위": result="짐"
if com =="보" and user=="보": result="비김"

print("나 : " + user)
print("컴 : " + com)
print("결과 : " + result)