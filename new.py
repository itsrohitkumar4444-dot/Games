import random 
upper_limit = int(input("enter the upper limit:"))
lower_limit = int(input("enter the lower limit:"))
if upper_limit<= lower_limit:
    number = random.randint(lower_limit, upper_limit)
    print("you have only 5 chances to guess the number")    
    for i in range(1,6):
        guess = int(input("Enter your Guess :"))
        if guess == number:
            print("Congratulations you guessed the number")
            break
        else:
            print("wrong guess")
            print(f"you have {5-i} chances left")
            if guess < number:
                print("your guess is low")
            else:
                print("your guess is high")
    print(f"You were unable to guess the number which is {number}")
else : 
    print("You have Entered larger lower limit than or equal to upper limit.")