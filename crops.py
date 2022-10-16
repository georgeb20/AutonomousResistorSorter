#import necessary libraries
import xmltodict
from PIL import Image
import os

ext = '.xml'#search for all .xml files in the directory
count=0 #initalize count to 0
for file in os.listdir(os.getcwd()): # iterating over all files
    
    if file.endswith(ext):
        f = open(file,'r')
        file_data = f.read() # read XML file contents
        parts = file.split(".xml") # return the file name
        img_name = parts[0]+'.jpg' # insert .jpg to file name
        image = Image.open(img_name) # open the image file
        dict_data = xmltodict.parse(file_data) #parse XML data
        bands = dict_data['annotation']['object'] # return the band data from the XML file
        bbox=[]
        for band in bands: # for each band
            bbox_all = band['bndbox'] # get the band coordinates
            #crop image based on the coordinates
            img_crop = image.crop(box=(int(bbox_all['xmin']),int(bbox_all['ymin']),int(bbox_all['xmax']),int(bbox_all['ymax']))) 
            img_crop.save('C:/Users/georg/OneDrive/Desktop/dump/bands2/'+str(count)+".jpg") # save image to directory
            count=count+1   #increase count
    else:
        continue
