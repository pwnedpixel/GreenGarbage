import src.stepperTest2 as motor

#Order is Red, Blue, Green.

redDistance = 200;
greenDistance=200;
dumpDistance=600;
right=2
left=-2

def dumpRed():
    print("red")
    # move to red
    motor.move(left,redDistance,"bottom")
    dump()
    # moveback
    motor.move(right, redDistance, "bottom")

def dumpGreen():
    print("green")
    motor.move(right,greenDistance,"bottom")
    dump()
    # moveback
    motor.move(left, greenDistance, "bottom")

def dumpBlue():
    print("Blue")
    dump()

def dump():
    print("dumping")
    #dump piece
    motor.move(2, dumpDistance, "top")
    motor.move(-2, dumpDistance, "top")
    #reset

def dropTo(colour):
    if (colour == 'red'):
        dumpRed()
    elif (colour == 'green'):
        dumpGreen()
    elif (colour == 'blue'):
        dumpBlue()


dropTo('red')
