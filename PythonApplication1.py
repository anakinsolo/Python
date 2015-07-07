import urllib.request
import re
import sys
from os.path import basename
from urllib.parse import urlsplit
from sys import argv

script, filename = argv

url=raw_input('?')
page =urllib.request.urlopen(url).read()

file=open(filename,w)

imgurls = re.findall(b'img .*?src="(.*?)"',page)
for x in range(0,3):
    print('Tuan yeu Thuy Anh')

for imgurl in imgurls:
    try:
        imgdata = urllib.request.urlopen(imgurl).read()
        fileName = basename(urlsplit(imgUrl)[2])
        file.write(imgData)
        file.close()
    except: 
        pass