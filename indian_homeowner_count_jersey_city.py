import urllib.request 
from bs4 import BeautifulSoup
import re

webUrl = urllib.request.urlopen('https://www.momjunction.com/articles/popular-indian-last-names-for-your-baby_00334734')
print ("result code: " + str(webUrl.getcode())) 
if (webUrl.getcode() == 200):
    data = webUrl.read()

    soup = BeautifulSoup(data, 'html.parser')
    header3 = soup.find_all('h3')

    
    # print(type(header3))
    # print(header3)
    last_name_clean = []

    for i in header3:
        if  ':' in str(i):
            last_name_clean.append((re.search('\.(.*):', str(i)).group(1)).strip())
            

    print (sorted(last_name_clean))
    total_count = 0
    indian_count = 0
    with open('C:\\temp\\0900monm140615\\0900monm140615.csv') as JCTaxRecFile:
        for line in JCTaxRecFile:
            for last_name in last_name_clean:
                if (last_name.upper() in line):
                    indian_count += 1
            total_count += 1
    print (total_count)
    print (indian_count)
    # print(head)

    # print (type(table_header))
    # df = pd.DataFrame(l, columns=["Symbol","Security","SEC filings","GICS Sector","GICS Sub Industry","Headquarters Location","Date first added","CIK","Founded"])
    # print(df['Symbol'])
    
else:
    print ("Received error, cannot parse results")
