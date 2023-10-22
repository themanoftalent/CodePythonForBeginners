import urllib.request
import random

def downloadApic(link):
    biased_file_name=random.randrange(1,10)

    full_name=str(biased_file_name)+'.jpg'
    urllib.request.urlretrieve(link,full_name)


downloadApic('https://timedotcom.files.wordpress.com/2014/03/scarlett-johansson.jpg')

#downloadApic('https://www.toptenselect.com/wp-content/uploads/2016/05/best-star-projectors.jpg')