import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*']

print("Welcome to Series wise password generator")

nr_letters = int(input("Enter number of letter you want in your password ? :"))
nr_numbers = int(input("Enter number of numbers you want in your password ? :"))
nr_symbols = int(input("Enter number of symbols you want in your password ? :"))

password = ""

for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password+=random_char
for num in range(0,nr_numbers):
    random_num=random.choice(numbers)
    password+=random_num
for sym in range(0,nr_symbols):
    random_sym=random.choice(symbols)
    password+=random_sym

print(password)