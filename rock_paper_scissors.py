import random
rock=0
paper=1
scissors=2

print("rock-0, paper-1, scissors-2")
random_num = random.randint(0,2)
avail=[0,1,2]

while True:
    user_ans=int(input("enter rock-paper-scissors(in numbers): "))
    if user_ans in avail:
        if user_ans==random_num:
            print("you tied!")
        
        elif (user_ans==0 and random_num==1):
            print("you lost!")
        
        elif (user_ans==0 and random_num==2):
            print("you win!")

        elif (user_ans==1 and random_num==0):
            print("you win!")
        
        elif (user_ans==1 and random_num==2):
            print("you lost!")
        

        elif (user_ans==2 and random_num==0):
            print("you lost!")
          
        elif (user_ans==2 and random_num==1):
            print("you win!")
    else:
        print("not in  option")