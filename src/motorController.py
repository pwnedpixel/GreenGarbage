import stepperTest2 as motor

#Order is Red, Blue, Green.

redDistance = 200;
greenDistance=180;
dumpDistance=600;
right=2
left=-2

def dumpRed():
    print("plastic")
    # move to red
    motor.move(left,redDistance,"bottom")
    dump()
    # moveback
    motor.move(right, redDistance, "bottom")

def dumpGreen():
    print("paper")
    motor.move(right,greenDistance,"bottom")
    dump()
    # moveback
    motor.move(left, greenDistance, "bottom")

def dumpBlue():
    print("garbage")
    dump()

def dump():
    print("dumping")
    #dump piece
    motor.move(2, dumpDistance, "top")
    motor.move(-2, dumpDistance+2, "top")
    #reset

def dropTo(colour):
    if (colour == 'plastic'):
        dumpRed()
    elif (colour == 'paper'):
        dumpGreen()
    elif (colour == 'garbage'):
        dumpBlue()

