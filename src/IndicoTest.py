from indicoio.custom import Collection
import PIL.Image
import numpy as np
import indicoio

open_file=open('../keys.txt','r')
file_lines=open_file.readlines()
key =file_lines[0].strip()
indicoio.config.api_key = key
collection = Collection("legoColor")
#
# #print(indicoio.image_recognition(pixel_array))
# # Image data
for x in range(0,6):
    print("Uploading "+str(x)+"...")
    image = PIL.Image.open('../images/green/'+str(x)+'.jpg')
    pixel_array = np.array(image)
 #   collection.add_data([pixel_array, "green"])
    print("...done")
# Training
#collection.train()
# Telling Collection to block until ready
collection.wait()
# Done! Start analyzing text
image = PIL.Image.open('../images/test.jpg')
pixel_array = np.array(image)
print(collection.predict(pixel_array))