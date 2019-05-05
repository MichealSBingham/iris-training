## Splits Image Data in Folders into Test, Train, Val Sets

from pathlib import Path
import os
from sklearn.model_selection import train_test_split
from shutil import copyfile
from shutil import move
import sys
from progress.bar import IncrementalBar
from tqdm import tqdm
import numpy as np

# python split.py imagesPath sizeOfTestingData destinationPath
def main():

    images_path = sys.argv[1]
    print("Path to Images : "+ str(images_path))
    size = float(sys.argv[2])
    dest = sys.argv[3]
    print("Path to Destination : "+ str(dest))
    X, Y = getAllImagePaths(images_path)
    X_train, Y_train, X_test, Y_test, X_val, Y_val  = split(X,Y, size)
    print("Done Spliting.")
    copyFiles(X_train, Y_train, X_test, Y_test, X_val, Y_val, dest)



#Size is the portion of testing dating to use ( size < 1)
#X - [Paths to Images] (array with paths to images) String
#Y - [Classification] (array with classification of image ) String
#Returns X_train, Y_train, X_test, Y_test, X_val, Y_val
def split(X, Y, size):
    print("Spliting....")

    """
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=size, random_state=1)
    X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=size, random_state=1)
    """
    X_train, x_remain = train_test_split(X, test_size=(size + size))
    new_test_size = np.around(size / (size + size), 2)
    new_val_size = 1.0 - new_test_size
    X_val, X_test = train_test_split(x_remain, test_size=new_test_size)

    Y_train, y_remain = train_test_split(Y, test_size=(size + size))
    new_test_size = np.around(size / (size + size), 2)
    new_val_size = 1.0 - new_test_size
    Y_val, Y_test = train_test_split(y_remain, test_size=new_test_size)

    print("Sizes \n . X Train: "  + str(len(X_train)) + "\nY_test: " + str(len(Y_test)) + "\n" +str(len(X_test)) + "\nY_val: " + str(len(Y_val)) )

    return X_train, Y_train, X_test, Y_test, X_val, Y_val


# Lists all absolute paths of each file in the directory
def getAllImagePaths(directory):
    X = []
    Y = []
    print("Getting paths of all images ...")

#    thisBar = IncrementalBar('Joining Image Paths', max=len(filenames), suffix = '%(percent).1f%% - %(eta)ds')

    for dirpath,_,filenames in tqdm(os.walk(directory)):
        for f in filenames:
            file =  os.path.abspath(os.path.join(dirpath, f)) #absolute file path
            class_name = os.path.split(os.path.dirname(file))[1]
            X.append(file)
            Y.append(class_name)
        #    thisBar.next()
            #sys.stdout.flush()
#    thisBar.finish()

    return X,Y

"""
def getArraysOfImagePaths(path):
    X = [] #Paths to Images
    Y = [] #Classification
    print("getArraysOfImagePaths .. ")
    counter = 0
    for file in getAllFilePaths(path):
        class_name = os.path.split(os.path.dirname(file))[1]
        X.append(file)
        Y.append(class_name)
        counter = counter + 1
        print("On image path: " + str(counter))
        sys.stdout.flush()
    return X, Y

    """

def copyFiles(X_train, Y_train, X_test, Y_test, X_val, Y_val, dest):
    ## Copy Training Data
    print("Copying Files...")

    bar = IncrementalBar('Copying Training Data', max=len(X_train), suffix = '%(percent).1f%% - %(eta)ds')
    for (path, class_name) in zip(X_train, Y_train):

        file_path = path
        file_name = os.path.basename(file_path)
        destination = dest+'/train/'+class_name+'/'+file_name
        try:
            try:
                os.mkdir(destination)
            except:
                pass
            move(file_path, destination)
        except:
            pass
        bar.next()
        sys.stdout.flush()
    bar.finish()

    ## Copy Testing Data
    bar2 = IncrementalBar('Copy Testing Data', max=len(X_test), suffix = '%(percent).1f%% - %(eta)ds')
    for (path, class_name) in zip(X_test, Y_test):

        file_path = path
        file_name = os.path.basename(file_path)
        destination = dest+'/test/'+class_name+'/'+file_name
        try:
            try:
                os.mkdir(destination)
            except:
                pass
            move(file_path, destination)
        except:
            pass
        bar2.next()
        sys.stdout.flush()


    bar2.finish()

    ## Copy Validation Data
    bar3 = IncrementalBar('Copy Validation Data', max=len(X_val), suffix = '%(percent).1f%% - %(eta)ds')
    for (path, class_name) in zip(X_val, Y_val):

        file_path = path
        file_name = os.path.basename(file_path)
        destination = dest+'/val/'+class_name+'/'+file_name
        try:
            try:
                os.mkdir(destination)
            except:
                pass
            move(file_path, destination)
        except:
            pass
        bar3.next()
        sys.stdout.flush()


    bar3.finish()


main()
