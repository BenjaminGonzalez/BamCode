import random
import string
import os.path


def thang():
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    f = "x"
    c = (6*a + b + a)
    d = a + b + f
    e = 6*d
    return c + " " + e

thang()
#print(thang())
#print(len(thang()))

def book():
    b = 27 * " "
    c = ""
    for i in range(round(125179/(27*2))):
        a = thang()
        if a not in ["UUUUUUIU UIxUIxUIxUIxUIxUIx", "llllllYl lYxlYxlYxlYxlYxlYx", "bbbbbbGb bGxbGxbGxbGxbGxbGx", "aaaaaaua auxauxauxauxauxaux", "BBBBBBJB BJxBJxBJxBJxBJxBJx"]:
            c += a + b
        #print (thang())
    return c
#print(book())

for i in range(40):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10)) + '.txt'
    print (name)
    path = 'C:/Users/I342505/Desktop/test/testdata/'
    complete = os.path.join(path, name)
    f = open(complete, 'w')
    f.write(book())
    f.close



#xxx = open('asyoulikeit.txt').read()
#print(len(xxx))
#charlength of book


'''
"UUUUUUIU UIxUIxUIxUIxUIxUIx",
"llllllYl lYxlYxlYxlYxlYxlYx",
"bbbbbbGb bGxbGxbGxbGxbGxbGx",
"aaaaaaua auxauxauxauxauxaux",
"BBBBBBJB BJxBJxBJxBJxBJxBJx"
'''

