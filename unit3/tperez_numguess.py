import random
end_point = int(input("Please input the end point of the range of numbers I\'ll pick from: "))
while end_point < 5:
    print("The end point is too low to calculate the number of remaining guesses.")
    end_point = int(input("Please input the end point of the range of numbers I\'ll pick from: "))
random_num = random.randint(1,end_point)
num_of_guess = 1
remaining_guess = int(end_point/5) 
print("You have {} guesses.".format(remaining_guess))
guess = int(input("Guess the number I\'ve chosen from 1 to {}: ".format(end_point)))
remaining_guess = remaining_guess - 1
while remaining_guess > 0 and guess != random_num:
    if guess < 1 or guess > end_point:
        print("{} isn't within my range...".format(guess))
        guess = int(input("Please guess the number I\'ve chosen FROM 1 TO {}: ".format(end_point)))
    elif guess > random_num:
        print("Too high.")
        guess = int(input("Guess the number I\'ve chosen from 1 to {}: ".format(end_point)))
        num_of_guess = num_of_guess + 1
        remaining_guess = remaining_guess - 1
    elif guess < random_num:
        print("Too low.")
        guess = int(input("Guess the number I\'ve chosen from 1 to {}: ".format(end_point)))
        num_of_guess = num_of_guess + 1
        remaining_guess = remaining_guess - 1
if num_of_guess == 1:
    print("WOW! You guessed my number, {}, on the first try! You're pretty lucky!".format(random_num))
elif remaining_guess > 0:
    print("Good job! It took you {} out of {} guesses to get {}.".format(num_of_guess,int(end_point/5),random_num))
elif remaining_guess == 0 and guess == random_num:
    print("Hmmm...It took you all {} guesses but you got it right.".format(num_of_guess))
elif remaining_guess == 0:
    print("You have used all of your {} guesses. You can not make any more guesses.".format(num_of_guess))
print("Game Over.")