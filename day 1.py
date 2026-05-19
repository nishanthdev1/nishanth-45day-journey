# %%
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

# %%
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

# %%
n=int(input())
total=0
for i in range(1,n+1):
    total+=i
    print("Sum=",total)


# %%
n=int(input())
for i in range(1,11):
    print(n,"X",i,"=",n*i)

# %%
n=int(int(input()))
isprime=True
if n<=0:
    isprime=False
else:
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break

if isprime:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

# %%
n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# %%
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)

# %%

n = int(input("Enter number: "))
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# %%
a = int(input())
b = int(input())
c = int(input())

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest =", largest)

# %%
n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


