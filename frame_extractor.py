## Frame Extractor 
## Micheal S. Bingham 
## Splits a video into the number of frames the video has 


import cv2 
import time 
import os
from os import listdir
from os.path import isfile, join
from shutil import move
import csv
from pathlib import Path


def trainTestOrVal(path):
        if 'test' in path:
                return 'test'
        elif 'train' in path:
                return 'train'
        else:
                return 'val'

def get_video_annotations():
	with open('ucf-annotations.csv', mode='r') as file:
		reader = csv.reader(file, delimiter=' ')
		return {rows[0]:[rows[1],rows[2], rows[3], rows[4], rows[5]] for rows in reader}




def output_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """

    head, video_file_name = os.path.split(input_loc)
    video_name_no_extention = os.path.splitext(video_file_name)[0]

    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        cv2.imwrite(output_loc + '\\' + video_name_no_extention + "-" + "%d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break



def convertAllVideosToFrames(path):
	print("Converting Videos to Frames...")
	for root, dirs, files in os.walk(os.path.abspath(path)):
		for file in files:
			file_path = os.path.join(root, file)
			print("File path: " + str(file_path))
			head, video_file_name = os.path.split(file_path)
			head2, video_class_name = os.path.split(head)
			parent, data_group_name = os.path.split(head2)
			video_name_no_extention = os.path.splitext(video_file_name)[0]
			#dest = path + '\\' + data_group_name + '\\' + video_class_name + '\\' + video_name_no_extention
			dest = str(file_path).replace('.mp4', '')
			print("video_file_nameFile : " + str(video_file_name))
			print("video_class_name : " + str(video_class_name))
			print("data_group_name : " + str(data_group_name))
			print("video_name_no_extention : " + str(video_name_no_extention))
			print("dest : " + str(dest))
			output_frames(file_path,dest)
			os.remove(file_path)




def moveNormalFramesOut(path):

	annotations = get_video_annotations()
	print("Moving normal frames out")
	for root, dirs, files in os.walk(os.path.abspath(path)):
		for file in files:
			file_path = os.path.join(root, file)
			#print("File path: " + str(file_path))
			head, frame_file_name = os.path.split(file_path)
			head2, frame_class_name = os.path.split(head)
			parent, data_group_name = os.path.split(head2)
			parent2, data_type_name = os.path.split(parent) #data_type_name val,test, train
			frame_name_no_extention = os.path.splitext(frame_file_name)[0]
		#	dest = path + '/' + data_group_name + '/' + video_class_name + '/' + video_name_no_extention
			
			try:
				video_name = str(frame_file_name.split('-')[0]) + '.mp4'
				#print("Video Name: " + video_name)

				frame_number = int(frame_file_name.split('-')[1].replace('.jpg', ''))
				#print("Frame Number: " + str(frame_number))

				#print(annotations[video_name])

				start_action1 = int(annotations[video_name][1])
				end_action1 = int(annotations[video_name][2])
				start_action2 = int(annotations[video_name][3])
				end_action2 = int(annotations[video_name][4])

				if (start_action1 <= frame_number <= end_action1 ) or (start_action2 <= frame_number <= end_action2 ):
					#Frame is during the event 
					print(str(start_action1) + ' <= ' + str(frame_number) + ' <= ' + str(end_action1) + '\t' + str(start_action2) + ' <= ' + str(frame_number) + ' <= ' + str(end_action2))
				else: 
					if (start_action1==-1 and end_action1==-1 and start_action2==-1 and end_action2==-1): 
						print("It's a normal frame. Do Nothing")
					else:		
						#print("ELSE!!!!!")
						dest_normal = path + '\\' + trainTestOrVal(file_path) + '\\' + "normal" + '\\' + str(frame_file_name.split('-')[0]) + '\\'
						if not os.path.exists(dest_normal):
							os.mkdir(dest_normal)
						print("Moving Frame...********************************************* to : " + str(dest_normal))
						move(file_path, dest_normal)


			except: 
				pass










def main(): 
	dataset_path = input("Enter the location of the video dataset (the one you just created): ")
	#convertAllVideosToFrames(dataset_path)
	moveNormalFramesOut(dataset_path)



main()

