# Cathal Butler - G00346889 - Graph Theory Project
# Thompson's used with the stunting algorithm that allows the matching of regular expressions.

# == Reference Links ===================================
# Ian McLoughlin - Lecture notes and videos
# https://brilliant.org/wiki/shunting-yard-algorithm/
# http://www.oxfordmathcenter.com/drupal7/node/628
# https://swtch.com/~rsc/regexp/regexp1.html


# Function to read a string and convert infix to postfix
def infix_to_postfix_conversion(infix):
    # Variables
    specials = {60: '^', '*': 50, '.': 40, '|': 30, '-': 30, '+': 30}
    postfix = ''
    stack = ''

    for char in infix:
        if char == '(':
            stack = stack + char  # if '('  add to the stack
        elif char == ')':
            while stack[-1] != '(':  # while the char at the end of the string:
                postfix = postfix + stack[-1]  # add from the end of the stack, to the postfix
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

# State class represents a state with two arrows, labelled by label.
# None is a label for representing "e" arrows
class state:
    label = None
    edge1 = None
    edge2 = None


# An NFA that is represented by its initial and accept states.
class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept


def compile(postfix_expression):
    nfa_stack = []

    # Loop through each char:
    for char in postfix_expression:
        if char == '.':
            # Last in, first out:
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()

            # Join them together
            nfa1.accept.edge1 = nfa2.initial

            # Push new NFA to the stack
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfa_stack.append(newnfa)
        elif char == '|':
            # Last in, first out
            # Pop two NFAs off the stack:
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            # Create a new initial state, connect it to initial states of the two NFAs popped from the stack.
            initial = state()  # blank state
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            # Create a new accept state, connecting the accept states of the NFA popped the stack, to the new state.
            accept = state()  # black accept state
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            # Push new NFA to the stack
            nfa_stack.append(nfa(initial, accept))
        elif char == '*':
            # pop a single NFA from the stack
            nfa1 = nfa_stack.pop()

            # Create new initial and accept states
            initial = state()
            accept = state()

            # Create new initial state to nfa1s initial state and the new accept state.
            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            # Join the old accept state to the new accept state and nfa1s initial state.
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            # Push the new NFA to the stack.
            nfa_stack.append(nfa(initial, accept))
        else:
            # Create new initial and accept states.
            accept = state()  # ACCEPT STATE
            initial = state()  # INITIAL STATE

            #  Join the initial state to the accept state using an arrow labelled char.
            initial.label = char  # Join with a label - whatever the char is
            initial.edge1 = accept  # point to the accept state

            # Push the new NFA to the stack
            newnfa = nfa(initial, accept)
            nfa_stack.append(newnfa)

    # nfa_stack should only have a single nfa at this point.
    return nfa_stack.pop()


def follows(state):
    # Create a new state
    states = set()
    states.add(state)

    # Check if state has arrows labelled e from it.
    if state.label is None:
        if state.edge1 is not None:
            # if there is an edge1, follow it
            states |= follows(state.edge1)
            # if there is an edge2, follow it
        if state.edge2 is not None:
            states |= follows(state.edge2)
    # Return the set of states.
    return states


def match(infix, string):
    # Use the shunting algorithm and compile the regular express
    postfix = infix_to_postfix_conversion(infix)
    nfa = compile(postfix)

    # Current set of states and the next set of states.
    current = set()
    nextone = set()

    # Loop through each char in the string
    for s in string:
        # Loop through the current set of states.
        for c in current:
            # Check if the state is labeled s
            if c.label == s:
                nextone |= follows(c.edge1)
        # Set current to next, and clear out next.
        current = nextone
        nextone = set()  # set back to a blank state.

    # Check if the accept state is in the set of current states.
    return nfa.accept in current


# Tests
infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)

# End of program
