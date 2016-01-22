userinput= input('Enter string or int or float:  ')
if isinstance (userinput,str):
	print "sring",userinput
elif isinstance (userinput,int):
	print "int",userinput
elif isinstance (userinput,float):
	print "You entered float:",userinput
