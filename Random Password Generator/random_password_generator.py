import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*']

print("Welcome to Random wise password generator")

nr_letters = int(input("Enter number of letter you want in your password ? :"))
nr_numbers = int(input("Enter number of numbers you want in your password ? :"))
nr_symbols = int(input("Enter number of symbols you want in your password ? :"))

# We should create a list instead of string to shuffle it's letters. 

password_list = []

for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password_list.append(random_char)
for num in range(0,nr_numbers):
    random_num=random.choice(numbers)
    password_list.append(random_num)
for sym in range(0,nr_symbols):
    random_sym=random.choice(symbols)
    password_list.append(random_sym)

print(password_list)

# This random function will help us to shuffle the whole list that we select.abs

random.shuffle(password_list)
print(password_list)

# Now we going to change this list into string.abs

password=""
for i in password_list:
    password+=i

print(password)