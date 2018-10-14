import re

with open('msglevel3', 'r') as txt:
    matches = re.findall(r'[a-z]{1,}([A-Z]{3})([a-z]{1})([A-Z]{3})[a-z]{1,}', txt.read())
    str = ""
    for match in matches:
        str += match[1]
    print(str)