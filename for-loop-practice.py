#muhammad zain mushtaq
#sp25-bbd-070

# 1) Print all even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# 2) Print each name in uppercase
names = ["zain", "ali", "awais", "usman"]
for name in names:
    print(name.upper())

# 3) Print numbers from 10 to 1 in reverse order
for i in range(10, 0, -1):
    print(i)

# 4) Print numbers divisible by 3
numbers = [2,3,5,7,8,9,11,12,14,15,17,18,20,21,24,26,27,30]
for num in numbers:
    if num % 3 == 0:
        print(num)

# 5) Print squares of numbers from 1 to 10
for i in range(1, 11):
    square=i**2
    print(square)

# 6) Convert Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
for temp in celsius_temps:
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")

# 7) Print multiplication table of 5
for i in range(5,100,5):
    print(i)

# 8) Find the sum of all numbers in a list
num_list = [3, 7, 9, 12, 15]
total = 0
for num in num_list:
    total += num
print(total)

# 9) Print each character of a string separately
text = "pakistan"
for char in text:
    print(char)

# 10) Print words with more than 5 letters
words = ["apple", "banana", "cherry", "date", "grapefruit"]
for word in words:
    if len(word) > 5:
        print(word)
