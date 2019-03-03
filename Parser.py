# Cathal Butler - G00346889 - Graph Theory Project
# Parser class
# https://brilliant.org/wiki/shunting-yard-algorithm/
# http://www.oxfordmathcenter.com/drupal7/node/628


# Defined function
# Function to read a string and convert infix to postfix
def infix_to_postfix_conversion(user_input):
    # Variables
    specials = {'*': 50, '.': 40, '|': 30}
    postfix = ''
    stack = ''

    for char in user_input:
        if char == '(':
            stack = stack + char  # if '('  add to the stack
        elif char == ')':
            while stack[-1] != '(':  # while he char at the end of the string:
                postfix = postfix + stack[-1]  # add to the postfix
                stack = stack[:-1]  # removing from the top of the stack
            stack = stack[:-1]  # remove the open '(' bracket from the stack
        elif char in specials:  # if the chars are in the dictionary process:
            # loop through the stack and check the precedence of each char, get the char provided, if none then 0) <= get char at the end of the stack[-1] if none then 0
            while stack and specials.get(char, 0) <= specials.get(stack[-1], 0):
                # remove from the top of the stack and add it to the postfix expression:
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + char  # push the special char onto the stack!!!

        else:
            postfix = postfix + char  # append postfix expression

    # if anything is left, push them onto the end of the postfix expression
    while stack:  # loop through the stack
        postfix = postfix + stack[-1]  # add to postfix
        stack = stack[:-1]  # removing from the top of the stack
    return postfix


# End infix_to_postfix_conversion function

# Main menu function
def main_menu():
    # Heading
    print("=======================================================================================")
    print("==========                        Cathal Butler                              ==========")
    print("==========   Parse the regular expression from infix to postfix notation     ==========")
    print("=======================================================================================")

    # user_input = input('\nPlease enter a some values ')

    user_input = "(a.b)|(c*.d)"  # hardcoded for testing

    print("Complete conversion from infix to postfix:\n ", infix_to_postfix_conversion(user_input))  # print output of infix convert
