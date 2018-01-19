"""
About the 5th attempt to write a script that changes erroneous GE files.

Sometimes, the GE files report a time that differs from when the particular
piece of data was actually recorded.  This script attempts to fix that by 
determining the correct time that should be in the GE file by parsing the 
filename (which is created based on the system time and not by communicating
with the error-prone GE instrument).  If the time reported in the data file is
over 10 minutes outside of the time suggested by the file name, this script will
edit the file contents accordingly.  

Author: Fangbo Yuan, 1/4/2018
fangboy@umich.edu

SPACING: TABS
"""

import csv
import codecs
import re
import os
import glob
import struct
import datetime
from datetime import datetime as dt

def main():
	""" SPECIFY ONE FILE TO EDIT FOR NOW """
	# path = 'Y:/GEROOFTOP/ForExport/Temp/'
	path = 'Y:/GESPOOFTOP/'
	# Open the file as a regular file instead of a CSV because the 
	# format of the GE CSV file is all messed up
	files = glob.glob(path+'*')
	newest = max(files, key = os.path.getmtime)
	
	# Obtain the correct date and time using the file name as the reference
	filename_datetime = os.path.basename(newest)[9:-4]
	print("date and time from file", filename_datetime)
	
	ymd, hm = filename_datetime.split('_')
	year = ymd[:4]
	month = ymd[4:6]
	day = ymd[6:8]
	hour = hm[:2]
	min = hm[2:4]
	filename_time_str = (year + '-' + month + '-' + day + ' ' + hour + ':' + min + ':00')
	print ("what's this", year, month, day, hour, min)
	# print("does this work?", dt.strptime(filename_time_str, '%Y-%m-%d %H:%M:%S'))

	# create a datetime object from the parsed filename
	time_modified = dt(int(year), int(month), int(day), int(hour), int(min))
	file_time = dt(2000, 1, 1)
	
	value = ''
	margin = datetime.timedelta(minutes=10)
	with open(newest, 'r+') as file:
		for row in file:
			print('initial row', row)
			row = row.strip()
			row = row.replace('\0', '')
			print('ROW CONTENTS', str(row))
			date_time, value = row.split(',')
			print('date', date_time)
			file_time = dt.strptime(date_time, '%Y-%m-%d %H:%M:%S')
	# the time in the file contents must be within +- 10 mins of the time from the
	# parsed filename
	if not(time_modified - margin <= file_time and file_time <= time_modified + margin):
		print("file being rewritten")
		with open(newest, 'w') as file:
			# try to rewrite the file
			file.write('\0\0\0' + filename_time_str + ',' + value + '\n')


if __name__ == '__main__':
	main()
