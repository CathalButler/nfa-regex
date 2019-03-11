# Cathal Butler - G00346889 - Graph Theory Project
# Thompson's Construction class

# == Help Links ======================================
# Ian McLoughlin - Lecture notes and videos
# https://swtch.com/~rsc/regexp/regexp1.html

class state:
    label = None
    edge1 = None
    edge2 = None


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
    return nfa_stack.pop()


print(compile("ab.cd.|"))
