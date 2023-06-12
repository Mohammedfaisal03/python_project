import random
random_number=random.randint(1,100)
# print(random_number)



def hard(random_number):
    should_continue = False
    chances = 5
    while not should_continue:
        your_number=int(input("guess your number "))
        if your_number ==random_number:
            print("you win ")
        elif your_number>random_number:
            print(f"enter low nubmer than {your_number} ")
            if chances ==1:
                should_continue=True
                print("you lost ")
            else:
               chances-=1
        elif your_number<random_number:
            print(f"enter the greater number than {your_number}")
            if chances == 1:
                should_continue = True
                print("you lost ")
            else:
                chances -= 1



def easy(random_number):
    should_continue = False
    chances = 10
    while not should_continue:
        your_number=int(input("guess your number "))
        if your_number ==random_number:
            print("you win ")
        elif your_number>random_number:
            print(f"enter low nubmer than {your_number} ")
            if chances ==1:
                should_continue=True
                print("you lost ")
            else:
               chances-=1
        elif your_number<random_number:
            print(f"enter the greater number than {your_number}")
            if chances == 1:
                should_continue = True
                print("you lost ")
            else:
                chances -= 1


choose=input("enter 'easy' for easy level, and 'hard' for hard level ")
if choose=="easy":
    easy(random_number)
else:
    hard(random_number)