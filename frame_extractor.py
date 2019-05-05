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


annotations = get_video_annotations()

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
        cv2.imwrite(output_loc + '/' + video_name_no_extention + "-" + "%d.jpg" % (count+1), frame)
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
	for root, dirs, files in os.walk(os.path.abspath(path)):
		for file in files:
			file_path = os.path.join(root, file)
			print("File path: " + str(file_path))
			head, video_file_name = os.path.split(file_path)
			head2, video_class_name = os.path.split(head)
			parent, data_group_name = os.path.split(head2)
			video_name_no_extention = os.path.splitext(video_file_name)[0]
			dest = path + '/' + data_group_name + '/' + video_class_name + '/' + video_name_no_extention
			print("video_file_nameFile : " + str(video_file_name))
			print("video_class_name : " + str(video_class_name))
			print("data_group_name : " + str(data_group_name))
			print("video_name_no_extention : " + str(video_name_no_extention))
			print("dest : " + str(dest))
			output_frames(file_path,dest)
			os.remove(file_path)






def moveNormalFramesOut(path):
	for root, dirs, files in os.walk(os.path.abspath(path)):
		for file in files:
			file_path = os.path.join(root, file)
			print("File path: " + str(file_path))
			head, frame_file_name = os.path.split(file_path)
			head2, frame_class_name = os.path.split(head)
			parent, data_group_name = os.path.split(head2)
			frame_name_no_extention = os.path.splitext(frame_file_name)[0]
		#	dest = path + '/' + data_group_name + '/' + video_class_name + '/' + video_name_no_extention
			
			try:
				video_name = str(frame_file_name.split('-')[0]) + '.mp4'
				print("Video Name: " + video_name)

				frame_number = int(frame_file_name.split('-')[1].replace('.jpg', ''))
				print("Frame Number: " + str(frame_number))

				start_action1 = annotations[video_name][1]
				end_action1 = annotations[video_name][2]
				start_action2 = annotations[video_name][3]
				end_action2 = annotations[video_name][4]

				
				if  (start_action1 <= frame_number <= end_action1) or (start_action2 <= frame_number <= end_action2):
					#The frame is during an event of action so keep it 
				else: 
					#Move it to normal folder 
					dest_normal = path + '/' + data_group_name + '/' + "normal" + '/' + video_name_no_extention
					move(file_path, dest_normal)


			except: 
				pass




def get_video_annotations():
	with open('annotations.csv', mode='r') as file:
		reader = csv.reader(file, delimiter=' ')
		return {rows[0]:[rows[2],rows[4], rows[6], rows[8], rows[10]] for rows in reader}






def getFrameNumberOfImage():
	return 0 



def main(): 
	inpt = input("Enter the location of the video: ")
	outpt = input("Enter where to output the frames: ")
	#output_frames(inpt, outpt) # Outputs videos as folder of frames in dataset 
	move_all_normal_frames_out(inpt)



main()

