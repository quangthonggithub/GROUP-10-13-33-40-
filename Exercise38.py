a=str(input('Name of month:'))
if a=='January' or a=='March' or a=='May' or a=='July' or a=='August' or a=='October' or a=='December':
    print('31 days')
elif a=='February':
    print('28 or 29 days ')
elif a=='April' or a=='June' or a=='September' or a=='November':
    print('30 days')
