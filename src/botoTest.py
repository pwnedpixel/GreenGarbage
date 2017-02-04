import boto3
import datetime
import os

#locations are garbage paper plastic

def upload(location):

    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    #i think this is the best place to change file name to date/time
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
    os.rename("image.jpg",filename)

    data = open(filename, 'rb')
    s3.Bucket('qh17' + location).put_object(Key=filename, Body=data)

    print("ran")

    os.remove(filename)
