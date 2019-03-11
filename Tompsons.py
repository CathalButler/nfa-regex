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
        accept = state()    # ACCEPT STATE
        initial = state()   # INITIAL STATE
        initial.label = char    # Join with a label - whatever the char is
        initial.edge1 = accept  # point to the accept state
        nfa_stack.append(nfa(initial, accept))
