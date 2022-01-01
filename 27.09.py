# v1 = float(input('>>'))
# v2 = float(input('>>>'))
# t = float(input('>>>>'))
# d = v1 * t + v2 *t
# print(d)
# print(d * 10 ** 3)

#  find leap years

# year = int(input('>>>>'))
# if year % 4 ==0 and year % 100 == 0 and year % 400 == 0:
#     print('leap year')
# elif year % 4 == 0 and year % 100 != 0:
#     print('leap year')
# elif year % 4 != 0:
#     print('not leap year')
# elif year % 4 == 0 and year % 100 == 0 or year % 400 != 0:
#     print('not leap year')




# while True:
#     num = int(input('enter positive number: '))
#     if num < 0:
#         print('finishet')
#         break



# while True:
#     num = int(input('enter even number: '))
#     if not(num % 2):
#         print(num ** 10)




# a = int(input('>'))
# d = int(input('>>'))
# n = int(input('>>>'))
# sum = 0
# i = 0
# while i < n : 
#     sum += a
#     a += d
#     i += 1
    
# 
# num = int(input('>>>>'))
# i = 2
# while i < num:
#     if num % i == 0:
#         print('False')
#         i += 1


# a = int(input('>>>>'))
# i = 1
# k = 101
# while a <= k :
#     a % 2 == 0
#     print(i)
#     i += 1
#     break
    
num = int(input("Enter a number ( greater than 1)")  
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")



