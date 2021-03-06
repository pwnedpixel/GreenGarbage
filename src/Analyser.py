from indicoio.custom import Collection
import indicoio
import operator
import PIL.Image
import numpy as np

open_file=open('../keys.txt','r')
file_lines=open_file.readlines()
key =file_lines[0].strip()
indicoio.config.api_key = key

def getType(imgPath):
    collection = Collection("plasticPaperGarbage")
    collection.wait()
    image = PIL.Image.open(imgPath)
    pixel_array = np.array(image)
    response = collection.predict(pixel_array)
    print(response)
    if (response['paper'] > 0.5):
        return 'paper'
    if (response['plastic'] > 0.5):
        return 'plastic'
    return 'garbage'
    #return(max({response['green'],response['blue'],response['red']}))

#print(getColor('../images/test.jpg'))
