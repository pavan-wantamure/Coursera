reports.py

#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment,title,paragraph):
    print("Generating Report")
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title,styles["h1"])
    report_body  = Paragraph(paragraph,styles["h2"])
    report.build([report_title,report_body])


**********************************************************************

4.2)


#!/usr/bin/env python3
import os
import datetime
import reports
import emails

def report_email(fruits_Dir):
   supplier_notes = ""
   for file in os.listdir(fruits_Dir):
      fruit_desc_list = []
      file_address = fruits_Dir + file
      try:
        filetype = file.split('.')[1]
        filename = file.split('.')[0]
      except:
         print("Unable to get the File Type for file:",file)
      if filetype == "txt":
        with open(file_address,'r') as fh_fruit:
          for line in fh_fruit.readlines():
            fruit_desc_list.append(line.strip())
      supplier_notes = supplier_notes + "name:" + fruit_desc_list[0] + "<br/>" + "weight:" + fruit_desc_list[1] + "<br/>" + "<br/>"
   print(supplier_notes)
   print("Generating PDF")
   today = datetime.date.today()
   title = "Processed Update on " + today.strftime("%b %d, %Y")
   print(title)
   reports.generate_report("/tmp/processed.pdf",title,supplier_notes)
   print("Emailing PDF")
   message = emails.generate_email("automation@example.com","student-00-9da88c2f2dc3@example.com","Upload Completed - Online Fruit Store",
                         "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                         "/tmp/processed.pdf"
                        )
   print("Send")
   emails.send_email(message)



def main():
    print("Calling report_email()")
    report_email("/home/student-00-9da88c2f2dc3/supplier-data/descriptions/")

if __name__ == "__main__":
   main()
