"""
About the 5th attempt to write a script that changes erroneous GE files.

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
	filename_datetime = os.path.basename(newest)[9:-4]
	print("date and time from file", filename_datetime)
	time_modified = dt.fromtimestamp(os.path.getmtime(path))
	# TODO: What is going on with this formatting??!!!?
	time_modified_str = dt.strftime(time_modified, "%#Y-%#m-%d %#H:%M:%S")
	print('time modified', time_modified_str)
	print("does this work?", dt.strptime(time_modified_str, '%Y-%m-%d %H:%M:%S'))

	file_time = dt(2000,1,1)
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
			# file_time = dt.strptime(date_time, '%Y-%m-%d %H:%M:%S %p')
			file_time = dt.strptime(date_time, '%Y-%m-%d %H:%M:%S')
	if not(time_modified - margin <= file_time and file_time <= time_modified + margin):
		with open(newest, 'w') as file:
			# try to rewrite the file
			file.write('\0\0\0' + time_modified_str + ',' + value + '\n')


if __name__ == '__main__':
	main()
