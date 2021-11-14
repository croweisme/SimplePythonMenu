#NON WORKING, see notes below
choice = ''
def initmenu():
    print("Choose an option:","Option 1","Option 2","Option 3"," Quit: 4", sep = '\n')
    choice = input('')
initmenu()
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
        initmenu()

#This program was made with kalebs suggestions, and we ralize now that it wont work becuase the global variable choice will never be changed by the local variable changing inside the initmenu() function. so it creates an infinite loop that constantly calls the menu because the choice input is never technically saved by the function 
#tl;dr Global vs Local variable issue