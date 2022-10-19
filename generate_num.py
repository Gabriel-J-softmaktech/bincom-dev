import random



# generates random 4 digits number of 0s and 1s
numbers = set(range(10))
randNum = random.randint(0, 9)
last_3 = random.sample(numbers - {randNum}, 3)
generated_number = str(randNum) + "".join(map(str, last_3))

print("Generated Random of 4 digit number:", generated_number)