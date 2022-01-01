i = 0
while i <= 10:
    print(i)
    i += 2

# i = 0
# while i <= 10:
#     print(i)
#     i += 2


# i = 100
# while i >= 0:
#     print(i)
#     i -=10
i = 0
prev = 10
next = 11
while i <= 8:
    newnext = (prev * next) ** .5
    prev = next
    next = newnext
    print(newnext)
    i += 1
  

   



