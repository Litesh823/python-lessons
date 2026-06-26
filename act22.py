# TYPE CONVERSION
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

sum1 = num1 + num2
print("Result before Conversion :", end=' ')
print(sum1)

num1 = int(num1)
num2 = int(num2)

sum2 = num1 + num2
print("Result after Conversion : ", end=' ')
print(sum2)