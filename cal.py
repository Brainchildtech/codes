R=float(raw_input("Enter the monthly installment:  "))
n=float(raw_input("Enter the number of months:  "))
i=float(raw_input("Enter the rate of interest:  "))

print "1.Interest in months"
print "2.Interest in quartely"
print "3.Interest in Halfyearly"
k=int(input("Enter your calculation in months/years: "))


k=n
while k<7:
	if (k==1):

		i=i/1200
		z=(1+i)**n
		V=R*((z)-1)
		P=1-((1+i)**(-1))
		X=V/P
		Interest=X-(R*n)
		print ("Maturity value:  "),X
		print ("Interest earned:  "),Interest
		break		


        if (k==2):
		i=i/400
		V=R*(((1+i)**n)-1)
		P=1-((1+i)**(-1/3))
		X=V/P
		Interest=X-(R*n)
		print ("Maturity value:  "),X
                print ("Interest earned:  "),Interest
   	       	break
	if (k==3):
		i=i/200
		
                z=(1+i)**n
                V=R*((z)-1)
                P=1-((1+i)**(-1/6))
                X=V/P
                Interest=X-(R*n)
                print ("Maturity value:  "),X
                print ("Interest earned:  "),Interest
                break           

