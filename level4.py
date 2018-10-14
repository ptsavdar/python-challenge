import urllib.request

nothing = '12345'
sum = int(nothing)
count = 0
while nothing != None and count < 400:
    response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)
    content = response.read()
    print(content.decode('utf-8'))
    nothing = content.decode('utf-8').split(" ")[-1]
    if 'Yes. Divide by two and keep going.' in content.decode('utf-8'):
       sum /= 2
    else:
        sum += int(nothing)
    count += 1
print(sum)
