#just used to find best camera position

import SimpleCV as scv

mycam = scv.Camera()

while(1):

    raw_input("ENTER")

    mycam.getImage().scale(640,480).save("img.jpg")
