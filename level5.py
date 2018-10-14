import pickle
import urllib.request

tmpfile = open('banner.p', 'rb')
tmp = pickle.load(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))

for line in tmp:
    print("".join([k * v for k,v in line]))
