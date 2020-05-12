#!/usr/bin/python3
import requests
import os
import sys
import threading
import time
import multiprocessing
t= ["https://api.github.com", "http://bilgisayar.mu.edu.tr/",
"https://www.python.org/", "http://akrepnalan.com/ceng2034",
"https://github.com/caesarsalad/wow"]
def getPID():
    return str(os.getpid())
def getavgld():
    if os.name=="posix":
       if int(os.cpu_count())-int(os.getloadavg()[1])<1:
          exit()
       return str(os.cpu_count())+":"+str(os.getloadavg()[1])
    else:
       return "This function can use only in linux"
def request(link):
    g=requests.get(link)
    print("request to:"+str(link)+" PID:"+str(getPID()))
    if int(g.status_code)>199 and int(g.status_code)<300:
        print("Site is valid code:"+str(g.status_code))
    else:
        print("Site is not valid code:"+str(g.status_code))
    print("Operation ending...")
    time.sleep(4)
f=list()
print(getavgld())
#Multithreading
for i in range(0,len(t)):
   f.append(threading.Thread(target=request,args=(t[i],)))
   f[i].start()
   f[i].join()
