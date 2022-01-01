# num = int(input("Enter the number: "))
# while num > 0:
#     even_number = 0
#     new_number = num % 10
#     if new_number % 2 == 0:
#            even_number += '1'
#     if new_number // 2 == 0:
#         even_number += '1'
# while num > 0:
#     odd_number = 0 
#     new_number2 = num % 10 
#     if new_number2 % 2 != 0:
#         odd_number += '1'
#     if new_number2 // 2 != 0:
#          odd_number += '1' 
    
# a = int(input('Enter the number: '))
# b = int(input('Enter the number: '))
# while True:
#     if a <= b:
#         print(a)
#         a += 1
#     else:
#          print(a)
#          a -= 1
#          break
         
# a = b = 'Some str'
# c = b = 1
# print(a==b)
# print(a is b)
# print(c is b)


num = (1,2,3,4,5,6,7,8,9,10)
even = 0
odd = 0
for i in num:
        if not i % 2:
            even += 1
        else:
            odd += 1
print('Total even number is',even)
print('Total odd number is ',odd)
    

    
