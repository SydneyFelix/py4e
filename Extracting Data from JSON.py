import urllib.request, urllib.parse, urllib.error
import json
#note wedidn't really get service url

url = input('input url:')
if len(url) < 3 : url ='http://py4e-data.dr-chuck.net/comments_1641508.json'

print('retrieving %s', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js :
    print('Failure to retrieve')
    print(data)
    quit()

print(json.dumps(js, indent = 4))
L = js.values()
print('*****this is/are the keys of js')
print(len(js.values()))
print(js.values())
print('retrieving %s', url)
L = []
for j in js['comments']:
    j=int(j['count'])
    print('appending %d'%j)
    L.append(j)

# print('retrieved %d characters'%c)
sam = sum(L)
count = len(L)
porma = f'sum={sam}  bilang={count}'
print('count: %d '%count)
print('sum: ',sam)
