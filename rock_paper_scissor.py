import random
print("ROCK PAPER SCISSOR")
print("Choose 0 for ROCK")
print("Choose 1 for PAPER")
print("Choose 2 for SCISSOR")

rock ='''
    _______
    ---'   ____)
          (_____)
         (_____)
         (____)
    ---.__(___)
 '''

paper = '''

        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)

'''

scissor= '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
'''

user = int(input("What do you choose?: "))

if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissor)
else:
    print("You are exceeding your Range ! ")


print("COMPUTER CHOOSE :")
computer = random.randint(0,2)

if computer==0:
    print(rock)
elif computer==1:
    print(paper)
else:
    print(scissor)

if user==0:
    if computer==0:
        print("DRAW")
    elif computer==1:
        print("Computer WINS")
    elif computer==2:
        print("User WINS")
    else: 
        print("Insufficient query")

elif user==1:
    if computer==0:
        print("USER WINS ")
    elif computer==1:
        print("DRAW")
    elif computer==2:
        print("Computer WINS")
    else: 
        print("Insufficient query")

elif user==2:
    if computer==0:
        print("Computer WINS")
    elif computer==1:
        print("USER WINS ")
    elif computer==2:
        print("DRAW")
    else: 
        print("Insufficient query")

else:
    print("ERROR")
