import urllib.request



# def download_file(download_url):


#     name='file.pdf'
#     urllib.request.urlretrieve(download_url,name)



# download_file('http://alex.smola.org/drafts/thebook.pdf')




def download_file(download_url):
    response = urllib.request.urlretrieve(download_url)
    file = open("document.pdf", 'w')
    file.write(response.read())
    file.close()
    print("Completed")


download_file('http://alex.smola.org/drafts/thebook.pdf')

