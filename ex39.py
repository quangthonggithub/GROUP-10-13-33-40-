n=int(input("enter a sound level (delcibel):"))
if n==130:
    print(n,"delcibels correspond to Jackhammer")
elif n==106:
    print(n,"delcibels correspond to Gas lawnmower")   
elif n==70:
    print(n,"delcibels correspond to Alarm clock")   
elif n==40:
    print(n,"delcibels correspond to Quite room")
elif 106<n<130:
    print(n,"delcibels is corresponding between Jackhammer and Gas lawnmower")
elif 70<n<106:
    print(n,"delcibels is corresponding between Gas lawnmower and Alarm clock")  
elif 40<n<70:
    print(n,"delcibels is corresponding between Quite room and Alarm clock")
elif n>130:
    print(n,"delcibels is higher than Jackhammer(130dB)")
elif n<40:
    print(n,"delcibels is lower than Quite room(40dB)")