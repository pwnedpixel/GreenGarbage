import SimpleCV as scv

def takePhoto(path, myCam):
    myCam.getImage().scale(960,720).save(path)
    #mycam.getImage().scale(640,480).save("img.jpg")
