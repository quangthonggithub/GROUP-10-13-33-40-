#a=Human Years
#b=Dog Years
a=int(input('Human Years:'))
if 0<=a<=2:
    b=a*10.5
elif a>2:
    b=21+(a-2)*4
elif a<0:
    print('Error')
print('Dog Years',b)
