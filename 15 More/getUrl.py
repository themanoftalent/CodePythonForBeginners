import urllib.request



def getPhoto(scarlett):
    name=input('Enter a name for photo ')
    print('Downloading')
    urllib.request.urlretrieve(scarlett,name)
    


getPhoto('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg')