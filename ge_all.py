""" 
*****SPACING: SPACES***** 
Created by Fangbo Yuan on Nov. 10, 2017
"""

import os
import time

def get_all_ge(dir):
    dose_dict = {}
    i = 1
    # go though all the files in the directory
    for file in os.listdir(dir):
        print(i)
        full_path = dir + '/' + file
        with open(full_path) as f:
            line = f.readline()
            dose_rate = line[23:-1]
            print(dose_rate)
            try:
                dose_rate = float(dose_rate)
            except:
                print('haha whoops lol')
            if dose_rate in dose_dict:
                dose_dict[dose_rate] += 1
            else:
                dose_dict[dose_rate] = 1
        i += 1

    for key in dose_dict:
        print (key, dose_dict[key])

def main():
    dir = "Y:/GEROOFTOP/ForExport/Temp"
    get_all_ge(dir)

if __name__ == "__main__":
    main()