import os

for dirpath, dirnames, filenames in os.walk('/Users/aisul/Documents/PP2/'):
    print('Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
