import urllib.request
import random



def jennifer(link): #welldone forget it again
    
        """ link will be as parameter and in download place"""
        fakename=random.randrange(1,100) 
        #giving numbers butit is integer so 
        name='jeniffer_aniston_'+str(fakename)+'.jpg' 
        #we use str
        urllib.request.urlretrieve(link,name) 
        #request url



jennifer('https://www.tarihtebugun.org/bidibidi_design/foto/jennifer_aniston_kimdir_dogum_tarihi636-tarihtebugun.jpg')