import re

with open('msglevel2', 'r') as txt:
    data = re.sub('[^0-9a-zA-Z]', '', txt.read())
    print(data)