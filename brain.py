# by Derek Goss 2014

def parse(text):
    text = text.lower()
    text = text.split(" ")
    return text

def interpret(text):
    text = parse(text)
    actions = ["calculate", "what", "google", "search", "email"]
    operators = ["add", "plus", "+", "subtract", "multiply", "times", "multiplied", "divided", "divide"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    keywords = {"action": [], "operator": [], "data": []}
    for x in text:
        if x in actions:
            keywords["action"].append(x)
        if x in operators:
            keywords["operator"].append(x)
        if x[0] in numbers:
            keywords["data"].append(x)
    return keywords

def process(text):
    keywords = interpret(text)
    try:
        # ADDITION
        if keywords["operator"][0] == "add" or keywords["operator"][0] == "plus" or keywords["operator"][0] == "+":
            counter = 0
            string = ""
            for x in keywords["data"]:
                counter += float(x)
                string += x + " + "
            newstring = string[:len(string)-2] + "= " + str(counter)
            return newstring

        #  MULTIPLICATION
        if keywords["operator"][0] == "multiply" or keywords["operator"][0] == "multiplied" or keywords["operator"][0] == "times":
            counter = 1.0
            string = ""
            for x in keywords["data"]:
                counter = counter * float(x)
                string += x + " * "
            newstring = string[:len(string)-2] + "= " + str(counter)
            return newstring

        #  DIVISION
        if keywords["operator"][0] == "divide" or keywords["operator"][0] == "divided":
            check = False
            counter = keywords["data"][0]
            string = ""
            for x in keywords["data"]:
                if check:
                    counter = float(counter) / float(x)
                check = True
                string += x + " / "
            newstring = string[:len(string)-2] + "= " + str(counter)
            return newstring
    except:
        "An error has occurred. Please try again."