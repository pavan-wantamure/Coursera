#!/usr/bin/env python3
import os
from PIL import Image
import sys

def process_images(image_Dir):

   for file in os.listdir(image_Dir):
      filename = file.split('.')[0]
      filename = filename + ".jpeg"
      try:
        im = Image.open(image_Dir+file).convert("RGB").resize((600,400))
        #im.convert("RGB")
        #im.resize((600,400))
        #print(im.size)
        im.save(image_Dir+filename,'JPEG')
      except:
        print("Could not Process File:",file)
        #print(sys.exc_Info()[0])
   print("All Images Processed")




def main():
    process_images("/home/student-03-4d2648dd874b/supplier-data/images/")


if __name__ == "__main__":
    main()
