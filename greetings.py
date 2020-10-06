import datetime

t=datetime.datetime.now().time()
hr=datetime.datetime.now().time().hour

if(hr>=12):
    print('Good Evening Good afternoon !!!!!')
else:
    print('Good Morning !!')

print(f"The Time is {t}")







