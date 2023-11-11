note=input("enter the name of the note: ")
letter=note[0]
num=int(note[1])
if letter=="C":
    d=261.63
if letter=="D":
    d=293.66
if letter=="E":
    d=329.63
if letter=="F":
    d=349.23
if letter=="G":
    d=392.00
if letter=="A":
    d=440.00
if letter=="B":
    d=493.88
d/=2**(4-num)
print(note, "has frequency is",d,"Hz")
