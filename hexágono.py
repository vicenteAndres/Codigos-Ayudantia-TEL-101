lado = int(input("Lado: "))
i=0
while i<lado:
    print(" "*(lado-(i+1))+"*"*(lado+2*i))
    i+=1
i-=2
while i>-1:
    print(" "*(lado-(i+1))+"*"*(lado+2*i))
    i-=1