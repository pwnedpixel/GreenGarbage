#import pygame
#import pygame.camera

#pygame.camera.init()
#cam = pygame.camera.Camera(0,(640,480))
#cam.start()
#img = cam.get_image()
#pygame.image.save(img,"filename.jpg")
#--------------------------------------------------
#doesnt work, claims that it wants string, not integer on line 5

import SimpleCV as scv

mycam = scv.Camera()

mycam.getImage().scale(640,480).save("img.jpg")
