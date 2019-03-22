# Cathal Butler - G00346889 - Graph Theory Project
# Parser class

# == Help Links ======================================
# https://brilliant.org/wiki/shunting-yard-algorithm/
# http://www.oxfordmathcenter.com/drupal7/node/628
# Ian McLoughlin - Lecture notes and videos


# Defined function


# Main menu function
def main_menu():
    # Heading
    print("=======================================================================================")
    print("==========                        Cathal Butler                              ==========")
    print("==========   Parse the regular expression from infix to postfix notation     ==========")
    print("=======================================================================================")

    # user_input = input('\nPlease enter a some values ')

    # user_input = "(a.b)|(c*.d)"  # hardcoded for testing

    # user_input = "(0 | (1(01 * (00) * 0) * 1) *) *"

    # == For testing: Oxford Website =====================================
    # user_input = "A*B+C"  # Test 1 -- A B * C +                   = PASS
    # user_input = "A+B*C"  # Test 2 -- A B C * +                   = PASS
    # user_input = "A*(B+C)"  # Test 3 -- A B C + *                 = PASS
    # user_input = "A-B+C"  # Test 4 -- A B - C +                   = PASS
    # user_input = "A*B^C+D"  # Test 5 -- A B C ^ * D +             = PASS
    # user_input = "A*(B+C*D)+E"  # Test 6 -- A B C D * + * E +     = PASS

    print("Complete conversion from infix to postfix:\n ",
          infix_to_postfix_conversion(user_input))  # print output of infix convert
