from indicoio.custom import Collection
import indicoio
import operator
import PIL.Image
import numpy as np

open_file=open('../keys.txt','r')
file_lines=open_file.readlines()
key =file_lines[0].strip()
indicoio.config.api_key = key

def getColor(imgPath):
    collection = Collection("legoColor")
    collection.wait()
    image = PIL.Image.open(imgPath)
    pixel_array = np.array(image)
    response = collection.predict(pixel_array)
    if (response['green'] > max({response['blue'],response['red']})):
        return 'green'
    if (response['blue'] > max({response['green'],response['red']})):
        return 'blue'
    if response['red'] > max({response['blue'], response['green']}):
        return 'red'
    return 'error'
   # return(max({response['green'],response['blue'],response['red']}))

print(getColor('../images/test.jpg'))