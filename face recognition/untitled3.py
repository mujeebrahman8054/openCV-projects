
from os import rename, listdir

folder = "C:\Users\MUJEEB\Desktop\open\test1"
fnames = listdir('.')

for fname in fnames:
    if fname.startswith(folder):
        rename(fname, fname.replace(name, '', 1))