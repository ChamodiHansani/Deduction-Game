play = True
while play == True:
    
    #Enter the name
    name = input("Enter your name:")

    #Display welcome to GameInt
    print("Hi" ,name, "Welcome to GameInt")
    print("Number to Guess - x x x x \t\t color maping: \n \t \t \t \t \t \t 1-white 2-blue 3-red \n \t \t \t \t \t \t 4-yellow 5-green 6-purple")
    print("Attempt No \t\t\t Guess \t\t\t Result \r")

    #Creating variables
    Number_List = [1,2,3,4,5,6]
    Result_List = [1,2,3,4]
    count = 0
    attempt = 1
    Result = 0
    User_List = []
    
    #Importing and Randomizing List
    import random
    Number_List=[]
    while count<4:
        num = random.randint(1,6)
        Number_List.append(num)
        count = count+1

    while Number_List != User_List and attempt <= 8:
        #Getting inputs
        print(attempt,end=" ")
        User_List = list(map(int,input(" \t\t\t\t ")))
        

        #Comparing Random List and User List
        if Number_List[0] == User_List[0]:
            Result_List[0] = "1"
        elif User_List[0] in Number_List:
            Result_List[0] = "0"
        else:
            Result_List[0] = "."

        if Number_List[1] == User_List[1]:
            Result_List[1] = "1"
        elif User_List[1] in Number_List:
            Result_List[1] = "0"
        else:
            Result_List[1] = "."
                    
        if Number_List[2] == User_List[2]:
            Result_List[2] = "1"
        elif User_List[2] in Number_List:
            Result_List[2] = "0"
        else:
            Result_List[2] = "."

        if Number_List[3] == User_List[3]:
            Result_List[3] = "1"
        elif User_List[3] in Number_List:
            Result_List[3] = "0"
        else:
            Result_List[3] = "."

        print("\t\t\t\t\t\t\t {} {} \n \t\t\t\t\t\t\t {} {}".format(Result_List[0],Result_List[1],Result_List[2],Result_List[3]))
        attempt = attempt + 1
        
    if Number_List == User_List :
        print("Congratulations!!! You have won the game")
    elif attempt > 8:
            print("You Lost")

    choice = input("Do you want to play again(Y/N): ")
    if choice.upper() == "Y":
        play = True
    elif choice.upper() == "N":
        play = False
        

    
