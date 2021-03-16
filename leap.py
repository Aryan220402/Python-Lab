n=int(input('Enter the Year'))
if n%4==0 :
	print('Leap year')
elif n%100==0:
	print('Leap year')
elif n%400==0:
	print('Leap year')
else :
	print('Not Leap year')