num = int(input('Enter number > 1'))
f = 0
i = 2
while i <= num /2:
    if num % i == 0:
        f=1
        break
    i+=1
if f==0:
    print('PRIME')
else:
    print('NOT PRIME') 
