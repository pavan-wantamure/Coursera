#!/usr/bin/env python3
import os
import requests


def upload_images(image_Dir):
   url = "http://localhost/upload/"
   for file in os.listdir(image_Dir):
       try:
          type = file.split('.')[1]
       except:
          print("Could Not upload File:",file)
          continue
       if type == "jpeg":
          with open(image_Dir+file,'rb') as f1:
              r = requests.post(url,files={'file':f1})



def main():
   upload_images("/home/student-03-4d2648dd874b/supplier-data/images/")



if __name__ == "__main__":
    main()


3)

#!/usr/bin/env python3
import os
import requests

def upload_fruits(data_Dir,image_Dir):
     fruit_description = {}
     url = "http://35.226.206.98/fruits/"
     for file in os.listdir(data_Dir):
         fruit_desc_list = []
         file_address = data_Dir + file
         try:
           filetype = file.split('.')[1]
           filename = file.split('.')[0]
         except:
           print("Unable to get the File Type for file:",file)
         if filetype == "txt":
            with open(file_address,'r') as fh_fruit:
                   for line in fh_fruit.readlines():
                       fruit_desc_list.append(line.strip())
            fruit_description["name"] = fruit_desc_list[0]
            fruit_description["weight"] = fruit_desc_list[1].split(" ")[0]
            fruit_description["description"] = fruit_desc_list[2]
            fruit_description["image_name"] = filename + ".jpeg"
            print("*****************")
            print(fruit_description)
            print("Uploading")
            response = requests.post(url,data=fruit_description)
            if response.ok:
                print("Successfully Posted")
            else:
                print("Upload Not Successfull")
                print("Status Code:",response.status_code)
                print("Text:",response.text)







def main():
   upload_fruits("/home/student-03-4d2648dd874b/supplier-data/descriptions/","/home/student-00-cccaeaf591ee/supplier-data/images/")


if __name__ == "__main__":
  main()
