import os
import glob
from pathlib import Path

source_files = glob.glob("U:\\Tests\\*.pdf")

for file in source_files:
    print(file)
    p = Path(file)
    name = p.stem   # without path or extension
    print(name)

    # TODO
    # analyse name to find matching files

    

# os.rename(file, new_name)
# dir = [ x.split('-')[2:] for x in source_files]
# dir = [ "".join(x) for x in dir ]

# https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python

# find pdfs from same book/id
# extract name
# sort [I, 1 .. 999, ]
# merge pdfs to one file

# appended by NameHelper




