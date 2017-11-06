# This program calculates the area of a region of interest in a spectra file.
# Spacing: TABS
import os
import time
import glob


def get_start_end():
	start = input("Select the starting channel, from 0 to 2047: ")
	end = input("Select the end channel, from 0 to 2047: ")
	return int(start), int(end)

def calc_area(counts_dict, start, end):
	# calculates the area of the region of interest demarcated
	# by the specified start and end
	chan_sum = 0
	i = start
	while i <= end:
		chan_sum += counts_dict[i]
		i += 1
	chan_sum -= (counts_dict[start] + counts_dict[start - 1] + counts_dict[start - 2]
	+ counts_dict[end] + counts_dict[end + 1] + counts_dict[end + 2])/6
	chan_sum *= (end - start + 1)
	return chan_sum
	
def main():
	# set path
	path = "Y:/roof_1958_spectra/"
	print('is the path right?', path)
	files = glob.glob(path+'*')
	newest = "Y:/roof_1958_spectra/ROOF_2017_10_12_T10_59.Spe"
	file_contents = ''
	with open(newest) as file:
		file_contents = file.readlines()[12:-14]
	counts = []
	for content in file_contents:
		content = content.replace('\n', '')
		content = content.replace(' ', '')
		counts.append(content)
	counts_dict = {}
	for i in range(len(counts)):
		counts_dict[i] = int(counts[i])
	print('counts_dict', counts_dict)
	start, end = get_start_end()
	print('start', start, 'end', end)
	print(type(start))
	while (start >= end):
		print("Please select a starting value that is"
		      " lower than the ending value.")
		start, end = get_start_end()
	area = calc_area(counts_dict, start, end)
	print("The area of the region of interest from channels", start, "to", end,
	      "is", area)
	time.sleep(5)

if __name__ == '__main__':
    main()
