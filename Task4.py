import random
print("~~~~~~~Welcome to Rock Scissors Paper Game")
user_score=0
comp_score=0
ties=0
name=input("Enter your name here :")
print("""
Winning Rules:    
1.Paper vs Rock --> Paper
2.Rock vs Scissors -->Rock
3.Scissors vs Paper --> Scissors
      """)
while True:
    print("""choices are:
    1.Rock
    2.Paper
    3.Scissors""")
    print()     
    choice=int(input("Enter your choice from 1 to 3 :"))
    print()
    while choice >3 or choice <1:
        choice=int(input("Enter valid input"))
    if choice ==1:
        user_choice="Rock"
    elif choice ==2:
        user_choice="Paper"
    else:
        user_choice="Scissors"
    print("The user's choice is",user_choice) 
    print("Now it is computer's turn") 
    computer=random.randint(1,3) 
    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"
    print("The computer choice is",comp_choice)
    if(user_choice=="Paper"and comp_choice=="Rock" or user_choice=="Rock" and comp_choice=="Paper" ):
        print("Paper Wins ")
        result="Paper"
    elif(user_choice=="Scissors"and comp_choice=="Rock" or user_choice=="Rock" and comp_choice=="Paper" ):
        print("Rock Wins")
        result="Rock"
    elif(user_choice==comp_choice):
        print("it's is a ties")
        result="ties"
    else:
        print("Scissors Wins")
        result="Scissors"
    if result=="ties":
        ties+=1
    elif result==user_choice:
        print("user wins")
        user_score+=1
    else:
        print("Computer Wins")
        comp_score+=1

    print("Score are :")
    print(name,"'s score  is:",user_score)
    print("computer score is :",comp_score)
    print("ties are ",ties)
    repeat=input("do you want to play again?")
    if repeat=="No":
        break
print("Game over!")
print("Thanks for playing")




