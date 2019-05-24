

#!/usr/bin/python

import os, sys
from os.path import dirname, abspath, basename, exists, splitext
from os.path import join as joinPath

DUPLICATE_MARKER = '1'
classes = ['Abuse', 'Arrest', 'Arson', 'Assault', 'Burglary', 'Explosion', 'Fighting', 'normal', 'RoadAccidents', 'Robbery', 'Shooting', 'Shoplifting', 'Stealing', 'Vandalism']



def flatten( here ):
    '''Move all files in subdirs to here, then delete subdirs.
       Conflicting files are renamed, with 1 appended to their name.'''
    for root, dirs, files in os.walk( here, topdown=False ):
        if root != here:
            for name in files:
                source = joinPath( root, name )
                target = handleDuplicates( joinPath( here, name )  )
                os.rename( source, target )

        for name in dirs:
           os.rmdir( joinPath( root, name ) )

def handleDuplicates( target ):
    while exists( target ):
        base, ext = splitext( target )
        target    = base + DUPLICATE_MARKER + ext
    return target


def main():

	train_path = joinPath('dataset', 'train')
	test_path = joinPath('dataset', 'test')
	val_path = joinPath('dataset', 'val')

	print("Flattening file structure ... ")

	#Flatten the files images in the train folder 
	print("Flattening train structure ... ")
	for category in classes: 
		class_path = joinPath(train_path, category)
		class_path = abspath(  class_path  )
		flatten(class_path)
	print("Flattening test structure ... ")
	for category in classes: 
		class_path = joinPath(test_path, category)
		class_path = abspath(  class_path  )
		flatten(class_path)
	print("Flattening val structure ... ")
	for category in classes: 
		class_path = joinPath(val_path, category)
		class_path = abspath( class_path )
		flatten(class_path)

	print("Done.")

main()
