 
p=float(raw_input("Enter the principal amount:  "))
r=float(raw_input("Enter the rate of interest:  "))
t=float(raw_input("Enter the number of period:  "))
k=5

if (k==1):
	

        n=1.0
        r=r/1200
        A=p*(1+(r/n))**(n*t)
        I=A-p
        print ("Maturity value for the fixed deosit: "), A
        print ("Interest earned Amount:  "),I
break


