miles = input('How many miles do you currently have? ')
if miles < 10000:
	print 'You do not have enough miles to make a redemption.'
elif miles < 19500:
	print 'You should redeem travel expenses totaling $' + str(format(float(miles)/100, '0.2f')) + ', but you will not have enough miles to save for a future redemption.'
else:
	print 'You should redeem travel expenses totaling $' + str(format((miles-10000)/0.95/100, '0.2f')) + '.'