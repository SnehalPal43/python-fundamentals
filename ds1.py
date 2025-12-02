# Q1.Write a program that asks the user for their name and age, then prints a sentence like:
# Hello Snehal, you are 21 years old!
name=input("enter your name:")
age=input("enter age:")
print("hello",name,",","you are",age,"years old!")

# Q2.Take two numbers as input from the user and print their:
# Sum, Difference, Product, Quotient
a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=a+b
difference=a-b
product=a*b
quotient=a/b
print(sum)
print(difference)
print(product)
print(quotient)

# Q3 Ask the user to enter two integers and one float.
# Convert them all to floats and print their average.
a=int(input("enter first num:"))
b=int(input("enter sec num:"))
c=float(input("enter third num:"))
a=float(a)
b=float(b)
avg=(a+b+c)/3
print(avg)

# Q4The user enters a string containing a number (e.g., "45").
# Convert it to:
# An integer
# A float
# A string again
# Print all three values with their types.
m=str(input("enter value of a:"))
a=str(m)
b=int(m)
c=float(m)
print("str value",a,type(a))
print("int value",b,type(b))
print("float value",c,type(c))

# Q5 Evaluate and print the result of the following expression:
# x = 10 + 3 * 2**2
# Based on what you learned in the lecture, explain why the output is what it is.
x = 10 + 3 * 2**2
print(x)


# Q6 Write a program to swap values of two numbers entered by the user.
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)

# Q7 Ask the user for a temperature in Celsius (string input).
# Convert it to float, then calculate and print the temperature in Fahrenheit.
# Formula:
# Fahrenheit = (Celsius * (9/5)) + 32
CelsiusTemp=int(input("enter temperature in celsius:"))
float_val=float(CelsiusTemp)
print("float value is:",float_val)
FahrenheitTemp=(CelsiusTemp*(9/5))+32
print("temp in Fahrenheit is:",FahrenheitTemp)

# Q8 ake the radius (r) as user input and print the area of a circle.
# Use the formula:
# Area = 3.14 * r * r
r=float(input("enter radius r:"))
Area=3.14*r*r
print(Area)

# Q9 Ask the user for: Principal (P), Rate (R), Time (T).
# Convert all to float and compute Simple Interest using:
# SI = (P * R * T) / 100
P=input("enter principal amount:")
R=input("enter rate of interest:")
T=input("enter time:")
P=float(P)
R=float(R)
T=float(T)
SI=(P*R*T)/100
print(SI)

# Q10 Take a decimal number as input (like 45.78) and output its:
# Integer part → 45
# Fractional part → .78
dec_num=input("enter decimal number:")
parts=dec_num.split(".")
integer_part=parts[0]
fractional_part="."+parts[1]
print("integer part is:",integer_part)
print("Fractional part is:",fractional_part)