# by Derek Goss 2014

import brain

greet = True  # determines greeting based off of whether the user has interacted for the first time yet
def greeting():
    global greet
    if greet:
        greet = False  # set after user uses for the first time
        return "Hello. How may I help you?  --("
    else:
        return "Anything else?  --("

def interact():
    loop = True  # switch for when to turn off loop/stop asking for input
    while loop:
        input = raw_input(greeting())
        if input.lower() == "no":
            break
        output = brain.process(input)
        print output

interact()
