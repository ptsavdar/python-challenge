import os
import zipfile

path, dirs, files = next(os.walk('./channel'))
file_count = len(files)
nothing = 90052
count = 0
zippy = zipfile.ZipFile('channel.zip')
comment = ""

while nothing is not None:
    response = open('./channel/' + str(nothing) + '.txt', 'r')
    comment += zippy.getinfo(str(nothing) + '.txt').comment.decode('utf-8')
    content = response.read()
    print(content)
    if 'Yes. Divide by two and keep going.' in content:
        nothing /= 2
    else:
        try:
            nothing = int(content.split(" ")[-1])
        except ValueError:
            nothing = None
    count += 1
    response.close()
print(count)
print(file_count)
print(comment)
