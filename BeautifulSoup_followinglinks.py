# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#correct in Testing phase
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
flag = True
url = input('Enter - ')
if len(url) < 5 : url = 'http://py4e-data.dr-chuck.net/known_by_Ayden.html'
for c in range(7): # seven is the number of times to repeat the process
    if flag == True:
        flag = False
        html = urlopen(url, context=ctx).read()
    else:
        html = urlopen(html, context=ctx).read()

    soup = BeautifulSoup(html, "html.parser")
    my_url = []
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:

            x = tag.get('href', None)
            # print(x)
            my_url.append(x)
            # print(my_url)
    print('***********************************************')
    html = my_url[17]  # because index 17 is the 18th being base zero
    for my in my_url[:18]:
        print(my)
