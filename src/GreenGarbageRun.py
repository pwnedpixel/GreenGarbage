import pic as cam
import Analyser
import motorController as MC
import botoTest as upload
import SimpleCV as scv

imgPath = "image.jpg"
mycam = scv.Camera()
while(1):
    raw_input("Press Enter")
    print("taking photo")
    cam.takePhoto(imgPath, mycam)

    print("analysing")
    #get the type
    itemType = Analyser.getType(imgPath)

    print("dropping")
    #drop
    MC.dropTo(itemType)

    print("uploading")
    upload.upload(itemType)
