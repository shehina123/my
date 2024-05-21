chislo=int(input('Enter a three-digit number: '))
dig1=chislo // 100
chislo=chislo-dig1*100
dig2=chislo // 10
dig3=chislo-dig2*10
s=dig1+dig2+dig3
if s==20:
    print('this is a Lucky number')
else:
    print('this is not a Lucky number')