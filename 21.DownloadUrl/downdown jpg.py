import urllib.request

def photoDown(url):
    name='newphoto.jpg'
    print('Beginning file download with urllib2...')
    urllib.request.urlretrieve(url, name)




photoDown('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg')