x=a=int(input("num: "))
y=b=int(input("num: "))
while (b>0):
        t=b
        b=a%b
        a=t
gcd=a
print ("gcd  of the two number is: "),a

lcm=(x*y)/a
print (" lcm of the two number is: "),lcm

