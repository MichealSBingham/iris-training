## Restore Original File Paths 
import os
from flatten import flatten 
from os.path import dirname, abspath, basename, exists, splitext
import csv
import shutil 



#Converts an array to a path
def toPath(path_array):
	path = ""
	for p in path_array:
		path = os.path.join(path, p)
	return path 

# Moves a file to a new path
def move(file, new_path):
	if not os.path.exists(new_path):
		os.makedirs(new_path)

	shutil.move(file, new_path)



def main():
	# Flatten the entire dataset 
	#flatten('dataset')

	csv_filename = input("Enter the name of the csv file with the original file paths: ")
	if '.txt' not in csv_filename:
		 csv_filename = csv_filename.strip() + '.txt'


	#Read each line in csv 

	with open(csv_filename) as csv_file: 
		reader = csv.reader(csv_file, delimiter = ',')
		counter = 0 
		for row in reader: 
			if (len(row) > 1):
				path_string = row[0]
				print(row)
				path = toPath(path_string.split('\\'))
				image = basename(path) #the name of the image etc 1001.jpg 
				image_path = os.path.join('dataset', image)
				move(image_path, dirname(path))
				counter = counter + 1 
				print("Now on file: " + str(counter))


	print("Done")


main()



