def dumpRed():
    print("red")
    # move to red
    dump()
    # moveback

def dumpGreen():
    print("green")
    # move to green
    dump()
    # moveback

def dumpBlue():
    print("Blue")
    #move to blue
    dump()
    #moveback

def dump():
    print("dumping")
    #dump piece
    #reset

def dropTo(colour):
    if (colour == 'red'):
        dumpRed()
    elif (colour == 'green'):
        dumpGreen()
    elif (colour == 'blue'):
        dumpBlue()
