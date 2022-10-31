import cv2
import numpy as np
from urllib.request import urlopen
from skimage import io
import csv

filename="imgtocheck.csv"
filetowrite = open('output.csv', 'w', newline='')
orgimg = cv2.imread("small.png")
orgimg2 = cv2.imread("small2.png")

def imgcompare(url):
    try:
        image = io.imread(url)
    except:
        print ("Source not found.")
        return True

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    width = 150
    height = 150
    dim = (width, height)
    resized = cv2.resize(image_rgb, dim, interpolation = cv2.INTER_AREA)

    b = resized
    difference = cv2.subtract(orgimg, b)    
    result = not np.any(difference) 
    difference2 = cv2.subtract(orgimg2, b) 
    result2 = not np.any(difference2) 
    
    if result is True:
        print("Pictures are the same")
        return True
    elif result2 is True:
        print("Pictures are the same")
        return True
    else:
        #cv2.imwrite("ed.jpg", difference )
        print("Pictures are different")
        return False


with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    writer = csv.writer(filetowrite)
    for row in datareader:
        inputkeyword=imgcompare(row[0])
        print(row[0])
        datatowrite=[inputkeyword]
        writer.writerow(datatowrite)
        

