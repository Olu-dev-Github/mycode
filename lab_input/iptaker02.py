#!/usr/bin/ebv python3
### Altar3 Research | Olu ###
### print() - concatenate vs print a series of items ###

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    device_vendor = input('Please enter vendor device name: ')
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
    print('Device vendors name is:  ', device_vendor)  
main()
