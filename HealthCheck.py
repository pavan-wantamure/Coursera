#!/usr/bin/env python3
import os
import psutil
import shutil
import socket
from emails import generate_health_check_email,send_email
from time import sleep

def check_cpu_health_ok():
   pct1 = psutil.cpu_percent()
   sleep(3)
   pct2 = psutil.cpu_percent()
   sleep(3)
   pct3 = psutil.cpu_percent()
   avg_pct = round((pct1 + pct2 + pct3 ) /3 )
   print("CPU Usage",avg_pct)
   return avg_pct


def check_diskspace_health_ok():
   total,used,free= shutil.disk_usage('/')
   disk_available_pct = ( free / total ) * 100
   if disk_available_pct >= 20:
     return 1
   else:
     return 0



def check_memory_health_ok():
   memory_stats = psutil.virtual_memory()
   if memory_stats[1] >= 500:
     print("Return 1, memory:",memory_stats[1])
     return 1
   else:
     print("Return 1, memory:",memory_stats[1])
     return 0



def check_local_host_ip_ok():
   ip = socket.gethostbyname("localhost")
   if ip == '127.0.0.1':
     print("Return 1, ip:",ip)
     return 1




def main():
   From = "automation@example.com"
   To = "student-03-4d2648dd874b@example.com"
   emailBody = "Please check your system and resolve the issue as soon as possible."
   print("Checking CPU")
   if check_cpu_health_ok() >= 80.0:
     subject_line = "Error - CPU usage is over 80%"
     print(subject_line)
     message = generate_health_check_email(From,To,subject_line,emailBody)
     send_email(message)
   if check_diskspace_health_ok() == 0:
     subject_line = "Error - Available disk space is less than 20%"
     message = generate_health_check_message()
     send_email(message)
   if check_memory_health_ok() == 0:
     subject_line = "Error - Available memory is less than 500MB"
     message = generate_health_check_message()
     #send_email(message)
   if check_local_host_ip_ok() == 0:
     subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
     message = generate_health_check_message()
     #send_email(message)




if __name__ == "__main__" :
   main()
