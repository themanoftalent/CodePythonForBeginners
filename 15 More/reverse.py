aStr = "drah reh skcuf fika"
thisislist = []

thisislist.extend(aStr)
print (''.join(thisislist))



size = len(thisislist)
print('The length of the string {}'.format(size))

for i in range(0,int(size/2)):

    thisislist[i], thisislist[size-1-i] = thisislist[size -1-i], thisislist[i]
print(''.join(thisislist).capitalize(),end='.\n')

