import urllib.request
import random

def a_photo(a_link):

    fake_name=random.randrange(1,100)
    name=str(fake_name)+'.jpg'
    urllib.request.urlretrieve(a_link,name)


a_photo('https://static.standard.co.uk/s3fs-public/thumbnails/image/2018/02/20/14/jenniferlawrence4.jpg')
