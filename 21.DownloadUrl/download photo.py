import urllib.request

def downdown(link):
    name='loop1.jpg'
    urllib.request.urlretrieve(link,name)


downdown('http://en.yesurdu.com/wp-content/uploads/2011/08/Scarlett-Johansson1.jpg')


