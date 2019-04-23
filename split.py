## Splits Image Data in Folders into Test, Train, Val Sets

from pathlib import Path
import os
from sklearn.model_selection import train_test_split
from shutil import copyfile
import sys

# python split.py imagesPath sizeOfTestingData destinationPath
def main():

    images_path = sys.argv[1]
    print("Path to Images : "+ str(images_path))
    size = float(sys.argv[2])
    dest = sys.argv[3]
    print("Path to Destination : "+ str(dest))
    X, Y = getArraysOfImagePaths(images_path)
    X_train, Y_train, X_test, Y_test, X_val, Y_val  = split(X,Y, size)
    print("Done Spliting.")
    copyFiles(X_train, Y_train, X_test, Y_test, X_val, Y_val, dest)



#Size is the portion of testing dating to use ( size < 1)
#X - [Paths to Images] (array with paths to images) String
#Y - [Classification] (array with classification of image ) String
#Returns X_train, Y_train, X_test, Y_test, X_val, Y_val
def split(X, Y, size):
    print("Spliting....")
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=size, random_state=1)
    X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=size, random_state=1)
    return X_train, Y_train, X_test, Y_test, X_val, Y_val

# Lists all absolute paths of each file in the directory
def getAllFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

def getArraysOfImagePaths(path):
    X = [] #Paths to Images
    Y = [] #Classification
    print("Gathering Image Paths")
    for file in getAllFilePaths(path):
        class_name = os.path.split(os.path.dirname(file))[1]
        X.append(file)
        Y.append(class_name)
        print(str(file) + " :" + str(class_name))
    return X, Y

def copyFiles(X_train, Y_train, X_test, Y_test, X_val, Y_val, dest):
    print("Copying Files...")
    ## Copy Training Data
    print("Copying Training Data...")
    for (path, class_name) in zip(X_train, Y_train):

        file_path = path
        file_name = os.path.basename(file_path)
        destination = dest+'/train/'+class_name+'/'+file_name
        print("Copying: " + str(file_path) + " Destination: " + str(destination) + "...")
        try:
            copyfile(file_path, destination)
        except:
            print("*****Couldn't copy  file: " + str(filename))
            pass

    ## Copy Testing Data
    print("Copying Testing Data...")
    for (path, class_name) in zip(X_test, Y_test):

        file_path = path
        file_name = os.path.basename(file_path)
        destination = dest+'/test/'+class_name+'/'+file_name
        print("Copying: " + str(file_path) + " Destination: " + str(destination) + "...")
        try:
            copyfile(file_path, destination)
        except error:
            print("*****Couldn't copy  file: " + str(filename))
            pass

    ## Copy Validation Data
    print("Copying Validation Data...")
    for (path, class_name) in zip(X_val, Y_val):

        file_path = path
        file_name = os.path.basename(file_path)
        destination = dest+'/val/'+class_name+'/'+file_name
        print("Copying: " + str(file_path) + " Destination: " + str(destination) + "...")
        try:
            copyfile(file_path, destination)
        except:
            print("*****Couldn't copy  file: " + str(filename))
            pass


main()
