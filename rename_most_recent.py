'''
The purpose of this program is to eliminate the inconvenience of 
MAESTRO writing over files every time a new data collection is
initiated.

Author: Fangbo Yuan
fangboy@umich.edu
'''

import os
import time
import glob
import datetime
from datetime import datetime as dt
import string 
time.sleep(4)

'''
This function searches for the newest file in 
the directory and subsequently renames it as the 
user specifies.

USAGE: 
path is a full directory path (e.g. Y:/something/other)

file_name_list is a list object of possible file names.  This
specifies the files whose names you want changed.

prefixes is a list object of new names for your files.
'''
	   
def find_and_rename(path, file_name_list, prefixes):
    #search for the newest file with extension .Spe
    #files = glob.glob(path+'*.Spe')
    print('is the path right?', path)
    files = glob.glob(path+'*')
    newest = max(files, key = os.path.getmtime)
    print("newest", newest)
    print("modified time", dt.fromtimestamp(os.path.getctime(path)))

    #rename the file according to the date and time
    #also, get rid of spaces and punctuation e.g. 7-31-1980 10:30
    #before adding the .Spe extention
    new_name = time.strftime("%Y_%m_%d_T")+time.strftime("%H_%M")
    i = 0
    while i < len(file_name_list):
        if (newest.startswith(file_name_list[i])):
            new_name = prefixes[i] + new_name + ".Spe"
            os.rename(newest, path + new_name)
            print('NEW NAME', new_name)
            print('renamed latest file')
            return
        i += 1

    print("no need to rename")
    return

def main():
    #set path
    path = "Y:/roof_1958_spectra/"
	
    #Please modify these two lists based on your lab room
    files = ['Y:/roof_1958_spectra\\OneHourBackground_ROOF', 'Y:/roof_1958_spectra\\OneHourBackground_1958']
    prefixes = ['ROOF_', '1958_']

    find_and_rename(path, files, prefixes)
    #display what you did on the screen for a bit
    time.sleep(3)
if __name__ == '__main__':
    main()