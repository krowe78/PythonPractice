print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Ok, Let's Play :)")
score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
        print('Correct!')
        score += 1
else:
    print("Incorrect!") 

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
        print('Correct!')
        score += 1
else:
    print("Incorrect!")

answer = input("What does cpu stand for? ")
if answer == "central processing unit":
        print('Correct!')
        score += 1
else:
    print("Incorrect!")

    print('Good job, your score is: '+ str(score))


        





