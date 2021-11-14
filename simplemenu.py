#The goal is to make a simple menu that lets me choose from 4 imaginary function options
#COMPLETE
#Now i need to learn how to add functions and things to a menu like this 
print("Choose an option:","Option 1","Option 2","Option 3"," Quit: 4", sep = '\n')
choice = input()
#variables assigned inside functions do not persist outside of funtions

#kaleb says instead of choice == value, make the function return a value and set the loop to check for function == value
#alternative, make the function return the input, and set choice = to the function 

#so choice = function()
#function()
    #yada yada yada ya
    #return a value

while True:
    if choice =='1':
        print("You have chosen option 1")
        break
    elif choice == '2':
        print("you Have Chosen Option 2")
        break
    elif choice == '3':
        print('You Have Chosen Option 3')
        break
    elif choice == '4':
        print("You Have Chosen to Quit, Exiting now")
        break
    else:
        print("You Have Selected an Invalid Option, Try again")
        print("Choose an option:","Option 1","Option 2","Option 3"," Quit: 4", sep = '\n')
        choice = input()

#SOURCE: https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
        
