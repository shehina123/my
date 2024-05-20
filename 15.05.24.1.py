T_AVG=18
h=bool(input('enter feeling'))#True/False
t=int(input('time of sleep'))
if t<T_AVG:
    print('sleeppy')
elif h and t>=T_AVG:
    print('hungry')
else:
    print('happy')