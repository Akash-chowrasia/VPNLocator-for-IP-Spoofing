import os

from time import sleep

import random

codeList = ["TR","US-C","US","US-W","CA","CA-W","FR","DE","NL","NO","RO","CH","GB","HK"]

try:

   os.system("windscribe connect")

   while True:

       choiceCode = random.choice(codeList)

       sleep(random.randrange(10,30))
       print("!!! Changing the IP Adress........")

       os.system("windscribe connect "+ choiceCode)

except:

   os.system("windscribe disconnect")

   print("sorry, some error has occured..!!")
