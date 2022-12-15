import random

top_of_range = input("Type in Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Hey stupid, type number larger than 0 next time!')
        quit()
else:
    print('Type in a digit next time. Hello!!!')        
    quit()





random_number = random.randint(0,top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print('You got it!!')
        break

    elif user_guess > random_number:
        print('You were above the random number...')    

    else:
        print('You were below the random number...')

print('You got it in ', guesses, 'guesses')


        
    
 













