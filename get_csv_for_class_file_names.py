import os
import csv


def getFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))



def get_image_class(file):
	if 'normal' in file: 
		return 'normal'
	elif 'Abuse' in file: 
		return 'Abuse'
	elif 'Arrest' in file: 
		return 'Arrest'
	elif 'Arson' in file: 
		return 'Arson'
	elif 'Assault' in file: 
		return 'Assault'
	elif 'Burglary' in file: 
		return 'Burglary'
	elif 'Explosion' in file: 
		return 'Explosion'
	elif 'Fighting' in file: 
		return 'Fighting'
	elif 'RoadAccidents' in file: 
		return 'RoadAccidents'
	elif 'Robbery' in file: 
		return 'Robbery'
	elif 'Shooting' in file: 
		return 'Shooting'
	elif 'Shoplifting' in file: 
		return 'Shoplifting'
	elif 'Stealing' in file: 
		return 'Stealing'
	elif 'Vandalism' in file: 
		return 'Vandalism'

def main(): 
	path = input("Enter the path of the dataset: ")
	with open('iris_frame_filepaths.txt', mode='w') as csvFile:
		iris_csv_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		counter = 0 

		for file_path in getFilePaths(path):
			counter = counter + 1 
			print("On file: " + str(counter))
			gs_path = file_path 
			if '.jpg' in file_path:
				#The file is an image 
				image_class = get_image_class(file_path)
				if image_class is not 'normal': 
					#Write the row 
					row = [gs_path, image_class, 'abnormal']
					iris_csv_writer.writerow(row)
				else:
					#Normal frame 
					row = [gs_path, 'normal']
					iris_csv_writer.writerow(row)

	print("Done.")

main()










