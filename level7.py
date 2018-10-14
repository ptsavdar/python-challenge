from PIL import Image

def ExtractMessage(carrier, outfile):
    c_image = Image.open(carrier)
    out = Image.new('L', c_image.size)
    width, height = c_image.size
    new_array = []
    msg = ""
    for h in range(height//2, height):
        for w in range(0, width, 7):
            ip = c_image.getpixel((w,h))
            if ip[0] == ip[1] == ip[2]:
                new_array.append(ip[0])
                if ip[0]:
                    msg += chr(ip[0])
            else:
                new_array.append(255)

    out.putdata(new_array)
    out.save(outfile)
    print("Message extracted and saved to " + outfile)
    print(msg)


ExtractMessage('oxygen.png', 'extracted.png')
