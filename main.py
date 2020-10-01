def displayIntro():
  #put an Introduction message to the users
  print("Welcome to the nonprofit page!")

def displayNonProfits():
  #print all the non-profits to the screen numerically. For Example:
#    1. World Central Kitchen
#    2. Crisis Text Line
#    3. Heart to Heart International
    list = ['World Central Kitchen', 'Crisis Text Line', 'Heart to Heart International']
    print (list[0])
    print (list[1])
    print (list[2])

def main():
    displayIntro()

    displayNonProfits()
    place = input("Which nonprofit would you like to donate to? ")

    totalwck = 0
    totalctl = 0
    totalhth = 0

    donate = int(input("How much money do you want to donate?"))

    if place == "World Central Kitchen":
        totalwck += donate
    elif place == "Crisis Text Line":
        totalctl += donate
    else:
        totalhth += donate

    print(totalwck)
    print(totalctl)
    print(totalhth)




    #steps: 
	#1. welcome the user using a unique Intro Message (use a function for this)
	#2. create a variable for each nonprofit/charity that keeps track of how much total money has been donated
	#3. display all the non-profits to the user and ask which one they would like to donate to 
	#4. then ask the user how much money they would like to donate to that specific charity chosen in step 3
	#5. update the variable created in step 2 with whatever amount the user wanted to donated
			#for example: missionbit = 0 -> user wants to donate 100 so you would add 100 to missionbit. missionbit is now 100
	#6. now display all the nonprofits with their new total amounts donated
    #7. repeat this process until the user wants to stop donating (only do this if you cover while loops)
	#push to github after every single step
main()