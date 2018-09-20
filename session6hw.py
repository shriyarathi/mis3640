# Write a program, greatest_common_divisor.py to implement this idea recursively. The function gcd() takes in two positive integers and returns one integer.

def gcd(a,b):
    if a == b:
        return a

    big = max(a, b)
    little = min(a, b)

    remainder = big % little
    
    if remainder==0:
        return little
    elif remainder==1:
        return 1
    else:
        return gcd(remainder, little)

print(gcd(2, 12))  # 2
print(gcd(17, 12)) # 1