from typing import Type
for i in range(1,101):
    a=''
    if i%5!=0 and i%3!=0:
        a=i
    if i%3==0:
        a='Fizz'
    if i%5==0:
        print(f'{a}Buzz')
        continue
    print(a)