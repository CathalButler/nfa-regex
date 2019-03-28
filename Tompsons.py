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
    specials = {'^': 60, '*': 50, '.': 40, '|': 30, '-': 30, '+': 30}
    postfix = ''
    stack = ''

    for char in infix:
        if char is '(':
            stack += char  # if '('  add to the stack
        elif char is ')':
            while stack[-1] != '(':  # while the char at the end of the string:
                postfix += stack[-1]  # add from the end of the stack, to the postfix
                stack = stack[:-1]  # removing from the top of the stack
            stack = stack[:-1]  # remove the open '(' bracket from the stack
        elif char in specials:  # if the chars are in the dictionary process:
            # loop through the stack and check the precedence of each char, get the char provided, if none then 0) <= get char at the end of the stack[-1] if none then 0
            while stack and specials[char] <= specials.get(stack[-1], 0):
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
class State:
    label = None
    edge1 = None
    edge2 = None


# An NFA that is represented by its initial and accept states.
class NFA:
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
            new_nfa = NFA(nfa1.initial, nfa2.accept)
            nfa_stack.append(new_nfa)
        elif char == '|':
            # Last in, first out
            # Pop two NFAs off the stack:
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            # Create a new initial state, connect it to initial states of the two NFAs popped from the stack.
            initial = State()  # blank state
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            # Create a new accept state, connecting the accept states of the NFA popped the stack, to the new state.
            accept = State()  # black accept state
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            # Push new NFA to the stack
            nfa_stack.append(NFA(initial, accept))
        elif char == '*':
            # pop a single NFA from the stack
            nfa1 = nfa_stack.pop()

            # Create new initial and accept states
            initial = State()
            accept = State()

            # Create new initial state to nfa1s initial state and the new accept state.
            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            # Join the old accept state to the new accept state and nfa1s initial state.
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            # Push the new NFA to the stack.
            nfa_stack.append(NFA(initial, accept))
        elif char is '+':
            # pop a single NFA from the stack
            nfa1 = nfa_stack.pop()

            # Create new initial and accept states
            initial = State()
            accept = State()

            # Create new initial state to nfa1s initial state and the new accept state.
            initial.edge1 = nfa1.initial

            # Join the old accept state to the new accept state and nfa1s initial state.
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            # Push the new NFA to the stack.
            nfa_stack.append(NFA(initial, accept))

        else:
            # Create new initial and accept states.
            accept = State()  # ACCEPT STATE
            initial = State()  # INITIAL STATE

            #  Join the initial state to the accept state using an arrow labelled char.
            initial.label = char  # Join with a label - whatever the char is
            initial.edge1 = accept  # point to the accept state

            # Push the new NFA to the stack
            new_nfa = NFA(initial, accept)
            nfa_stack.append(new_nfa)

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
    next_one = set()

    # Add current set of states and next set of states
    current |= follows(nfa.initial)

    # Loop through each char in the string
    for s in string:
        # Loop through the current set of states.
        for c in current:
            # Check if the state is labeled 's'
            if c.label == s:
                next_one |= follows(c.edge1)
        # Set current to next, and clear out next.
        current = next_one
        next_one = set()  # set back to a blank state.

    # Check if the accept state is in the set of current states.
    return nfa.accept in current


# List of tuples:
tests = [
    ('a+', ''),
    ('a.b.c*', 'abc'),
    ('a.(b|d).c*', 'abc'),
    ('(a.(b|d))*', 'abbc'),
    ('a.(b.b)*.c', 'abcc')
]
# Loop through each tuple in the list and run the match function to check the postfix expression to the string
for exp, res in tests:
    print(match(exp, res), exp, res)
