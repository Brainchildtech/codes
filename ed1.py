balance =4213
month=0.04
annual=0.2
total = 0
for i in range(1, 13):
    minipay = balance * month
    balance = (balance - minipay) * (1 + annual / 12.0)
    total += minipay
    print 'Month:', i
    print 'Minimum monthly payment:', round(minipay, 2)
    print 'Remaining balance:', round(balance, 2)
    
print 'Total paid:', round(total, 2)
print 'Remaining balance:', round(balance, 2)
