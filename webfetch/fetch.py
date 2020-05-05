from bs4 import BeautifulSoup
import urllib.request
import re

# example used in screenshots: https://arstechnica.com/gaming/2020/05/steam-data-points-to-massive-half-life-bump-in-vr-adoption/
inputLink = input("input link: ")
html_page = urllib.request.urlopen(inputLink)
soup = BeautifulSoup(html_page,"lxml")
content=soup.prettify()
i=0
htmlFile = open('html'+str(i),'w')
htmlFile.write(content)
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    i=i+1
    print (link.get('href'))
    level2 = urllib.request.urlopen(link.get('href'))
    soup2 = BeautifulSoup(level2,"lxml")
    content2 = soup2.prettify()
    htmlfile2 = open('html'+str(i),'w')
    htmlfile2.write(content2)
