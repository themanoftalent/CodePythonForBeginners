import sys
import path

my_file_path=path
print('Shows where my file is located')
print(my_file_path)


print('')

for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
