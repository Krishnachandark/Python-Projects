print("welcome to my computer quiz")
playing = input("do you want to play")
if playing != "yes": quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ") 
if answer == "central processing unit":
    print('Correct!')
else: 
    print('incorrect')
    answer = input("What does GPU stand for? ") 
if answer == "graphics processing unit":
    print('Correct!')
else: 
    print('incorrect')
    answer = input("What does RAM stand for? ") 
if answer == "ramdam access memory":
    print('Correct!')
else: 
    print('incorrect')
    answer = input("What does PsU stand for? ") 
if answer == "power supply unit":
    print('Correct!')
else: 
    print('incorrect')
    
    