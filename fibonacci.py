
a, b = 0, 1

# Check if 'b' is equal to 50 if its not re-assign variable a=b and b = a+b
while b < 50:
    print(b)
    a, b = b, a+b


