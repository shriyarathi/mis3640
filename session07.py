#iterations 

#1.1

result = 0

for i in range(1,11):
    print('current number to be added', i+1)
    print(i+1)
    result = result + i + 1
    #print('new result after this iteration:', result)


print (result) 


#1.2

for i in range(1,1001):
    print('current number to be added', i+1)
    print(i+1)
    result = result + i + 1
    #print('new result after this iteration:', result)

print(result)


#1.3
#odd

for i in range(1,1001):
    if i % 2 == 1:
        result = result + i 

print('The sum of odd numbers is,' result)

#even


for i in range(1,1001):
    if i % 2 == 0:
        result = result + i 

print('The sum of even numbers is,' result)


# for loop for factorial 10 

result = 1

for i in range(1,11):
    result = result * i

print('the factorial of 10 is,' result)    


def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print ('blastoff!')