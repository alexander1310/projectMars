day = 1
person = 10
food = 50
water = 100
mood = 100

endMsg = "\nThe crew goes to bed."

def printDay(day):
    print("\n========================= DAY", day, "=========================\n")

def printState(food, water, person):
    print("food:" +str(food) + ", water:", water, ", crew:", person, "\n") 

def printEndOfDay(message):
        # print("\n")
        print("\n\n" + message + "\n" + endMsg)   

intro = "Welcome human. I am PyTh0n an artificial intelligence, I will help you survive on this hostile envrionnement in Mars where you are."

playerName = input( intro + "\nBut first tell me: whats your name ? ")
message =  ""

while(food != 0 and water != 0):
    if day == 1:
        printDay(day)
        printState(food, water, person)

        step1 = eval(input("Hello "+ playerName +", Welcome on board.\n\nAs you are the commander here what do you want us to do ? (type the number to choose an action) \n1) Let's explore the planet. \n2) It's time to clean up the spaceship.\n"))
        
        if step1 == 1: 
            person = person - 1
            food = food - person*1
            water = water - person*2 + 5
            mood = mood - 20
            message = "There was an accident and a rock killed 1 person but you found some water :)."
            
        elif step1 == 2:
            person = person
            food = food - person*1
            water = water - person*2
            mood = mood + 20
            message = "Now the spaceship is clean and your team as satisfied" #TODO add message for option 2 in step 1

        printEndOfDay(message)
        day = day + 1

    elif day == 2:
        printDay(day)
        printState(food, water, person)
        
        print("Second day - Hello " + playerName + " I hope your first day on Mars went well.")
       
        step2 = eval(input("It's your second day. What do you want to do? \n1) Explore the planet again. \n2) Send a robot to check environement\n")) #TODO add new choices

        if step2 == 1:
            mood = mood - 40
            person = person - 2
            food = food - person*1
            water = water - person*2
            message = "We have a sand storm and two of your team sufocate." 

        elif step2 == 2:
            mood = mood + 10
            person = person
            food = food - person*1
            water = water - person*2
            message = "The robot finishes to check the environement and tells you not to explore further because a sandstorm is coming. Your team played cards." 

        printEndOfDay(message)
        day = day + 1

    elif day == 3:
        printDay(day)
        printState(food, water, person)
        
        print("Third day - Hello " + playerName + " I hope your second day on Mars went well.")

        step3 = eval(input("What do you want to do? \n1) You make a scientifice experience you study the ground on mars. \n2) You send a 2 person and 1 robot at exploration without the spaceship."))
        
        if step3 == 1:
            mood = mood + 50
            person = person
            food = food - person*1
            water = water - person*2
            message = "You discover a new bacteries speaces and you prove he have life on mars and is possibly to live her." 

        elif step3 == 2:
            mood = mood - 40
            person = person - 2
            food = food - person*1
            water = water - person*2
            message = "The robot come back and tell you the 2 members died in a sandstorm." 

        printEndOfDay(message)
        day = day + 1

    elif day == 4:
        printDay(day)
        printState(food, water, person)
        
        print("Fourth day - Hello " + playerName + " I hope your third day on Mars went well. The sand storm is over.")

        step4 = eval(input("What do you want to do? \n1) You go out the spaceship and go explorate with a robot. \n2) You stay in the spaceship and speaking with a crew for solution.\n")) 

        if step4 == 1:

            mood = mood + 20
            person = person 
            food = food - person*1
            water = water - person*2
            message = "You discover a tunnel made by ancient lava flows and you discover he have ice in the tunnel. "

        elif step4 == 2:
            mood = mood + 10
            person = person
            food = food - person*1
            water = water - person*2
            message = "You find a solution if there is one problem. "

        printEndOfDay(message)      
        day = day + 1
        

        




