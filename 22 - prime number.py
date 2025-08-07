print("****************************************")

num = 37

if num <= 1:
    print(num, "is not a prime number")
else:
   # check for factors
   for i in range(2,num):
       print(i)
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

print("****************************************")

if num <= 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,(num//2)+1):
       print(i)
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

print("****************************************")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        print(i)
        if num % i == 0:
            return "No"
    return "Yes"

print(f"Is 15 prime? {is_prime(15)}")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 25 prime? {is_prime(25)}")
print(f"Is 29 prime? {is_prime(29)}")
print(f"Is 37 prime? {is_prime(37)}")
print(f"Is 45 prime? {is_prime(45)}")


print("****************************************")
print("****************************************")