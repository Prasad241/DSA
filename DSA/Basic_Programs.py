# 1. WAP to Calculate Sum of The Given Numbers

# num=int(input("Input Numbers:"))
# sum=0
# while(num>0):
#     sum+=num%10
#     num=num//10
# print(sum)

# 2. WAP to check Whether a Number Palindrome or not

# num=int(input("Input Number:"))
# sum=0
# n=num
# while(num>0):
#     sum=sum*10 + (num%10)
#     num//=10
# if(n==sum):
#     print("Number is Palindrome")
# else:
#     print("Not Palindrome")

# 3. WAP to check Armstrong NO

# num=int(input("Enter Number:"))
# p=len(str(num))
# sum=0
# n=num
# while(num>0):
#     sum=sum +(num%10)**p
#     num//=10
# if (n==sum):
#     print("Armstrong") 
# else:
#     print("Not Armstrong!")   


# 4. Cube sum of n Natural Numbers

#1st Method
# sum=0
# n=int(input("Input Number: "))
# sum=(n*(n+1)//2)**2
# print(sum)

#2nd Method
# sum=0
# n=int(input("Input Number: "))
# for i in range (1,n+1):
#     sum+= i**3
# print(sum)

# 5. WAP to print pyramid pattern 

#Pattern 1
# n=5
# for i in range (1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()   

#Pattern 2
# n=5
# for i in range (n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()        

#Pattern 3
n=5
for i in range (1, n+1):
    for j in range(n, i-1, -1):
        print(j, end=" ")
    print()     