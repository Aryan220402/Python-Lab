h=10
r=5
f=10
t=eval(input('Enter the Time'))
Vtank=3.14*r*r*h
Vwtr=f*t
if Vwtr>Vtank :
    print('Over Flow')
    print('Volume :',Vwtr-Vtank)
elif Vwtr==Vtank :
    print('Tank Full')
else :
    print('UnderFlow Condition')
    ht=Vwtr/(3.14*r*r)
    hr=h-ht
    print(f'Filled Height : {ht}\nRemaining Height : {hr}')
