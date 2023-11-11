a=int(input('Enter Day:'))
b=str(input('Enter Month:'))
if a==1 and b=='January':
    print('New year’s day')
elif a==1 and b=='July':
    print('Canada day')
elif a==25 and b=='December':
    print('Christmas day')
else:
    print('month and day do not correspond to a fixed-date holiday')