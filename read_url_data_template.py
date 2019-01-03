import urllib.request 

webUrl = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
print ("result code: " + str(webUrl.getcode())) 
if (webUrl.getcode() == 200):
    data = webUrl.read()
    print(data)
else:
    print ("Received error, cannot parse results")
