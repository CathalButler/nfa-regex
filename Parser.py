# Cathal Butler - G00346889 - Graph Theory Project
# Parser class

# Variables
operation = []
output = []
token = []
i = 1


# Defined function
# Function to read a string and convert infix to postfix
def infixcoventer(user_input):
    for char in user_input:
        print(char)
        # Pass chars into token list:
        token = char

        # of token is white space skip it
        if token is ' ':
            continue

        # if its a number it to the queue
        if token.isalpha() or token.isdigit():
            output.append(token)



# End infixconveter function

# Function to return the order or precedence of operators via numbers 1-3:
def precedence(token):
    ##if token is '*' || token is '.' || token is '|':
       ## while operation != 0 &&
     ##       if not operation:



# end precedence function

def order_of_precedence:
    ##if token is '*'

# Main menu function
def mainmenu():
    # Heading
    print("=======================================================================================")
    print("==========                        Cathal Butler                              ==========")
    print("==========   Parse the regular expression from infix to postfix notation     ==========")
    print("=======================================================================================")

    user_input = input('\nPlease enter a some values ')

    infixcoventer(user_input)


# End mainmenu function.

# Called function
# Run main menu
mainmenu()
