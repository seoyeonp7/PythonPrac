def addminmuldiv(a,b):
    return a+b,a-b,a*b,a/b

sum,min,mul,div = addminmuldiv(5,4)
sum2 = addminmuldiv(5,4)

print("sum",sum)
print("min",min)
print("mul",mul)
print("div",div)

#튜플
print("sum2",sum2) 
print("sum2[0]",sum2[0])