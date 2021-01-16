import numpy as np
import cv2
import math  
import os
import xml.etree.ElementTree as ET
for filename in os.listdir("C:/python/showGR/"): 
    filename=os.path.splitext(os.path.basename(filename))[0]
    print(filename)
    tree = ET.parse("C:/python/showGR/"+filename+'.xml')
    root = tree.getroot()
    img = cv2.imread("C:/python/showGR/"+filename + ".jpg")
    for objects in tree.iter('object'):
       for doc in objects.findall('bndbox'):
        xx1=int(doc.find('xmin').text)
        xx2=int(doc.find('xmax').text)
        yy1=int(doc.find('ymin').text)
        yy2=int(doc.find('ymax').text)
        print(xx1,"  ",xx2,"  ",yy1,"  ",yy2)
        cv2.polylines(img,[np.array([(xx1,yy1),(xx1,yy2),(xx2,yy2),(xx2,yy1)])],True,(0,255,0),2)
        cv2.imwrite("C:/python/showGR/"+filename + "G.jpg",img)        