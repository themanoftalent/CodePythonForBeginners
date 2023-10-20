import os

# os.chdir('/Users/darwin/Desktop/MyCorrey')

# print(os.getcwd())

# for f_num,f_name in enumerate(os.listdir()):
# 	print('{}-{}'.format(f_num,f_name))

myfile="/Users/darwin/Desktop/MyCorrey/nsa.py"

## If file exists, delete it ##
if os.path.isfile(myfile):
    os.remove(myfile)
else:    ## Show an error ##
    print("Error: %s file not found" % myfile)
 