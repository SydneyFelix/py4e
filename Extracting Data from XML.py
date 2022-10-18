import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('input url:')
if len(url) < 5 : url = 'http://py4e-data.dr-chuck.net/comments_1641507.xml'
sam = 0
stuff = urllib.request.urlopen(url).read().decode()#trees is a long string
data = ET.fromstring(stuff)
tags = data.findall('comments/comment') # xml tree

for tag in tags:
    sam +=int(tag.find('count').text)
    print(sam)
