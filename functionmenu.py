def initmenu():
    print("Choose an option:","Option 1","Option 2","Option 3"," Quit: 4", sep = '\n')
    return input('')
choice = initmenu()

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
        choice = initmenu()

#initialize choice at the top, within init menu set choice = to input, then call initmenu()instead of setting choice = to initmenu()

#SOURCE: Kaleb's brain, thankyou Kaleb
#I couldn't figure out on my own how to make a function return a value and have that returned value persist until Kaleb pointed out that I could just set the function = to a variable
#Can't believe I didn't think of it earlier
#Now that he's pointed it out it seems so stupidly obvious 