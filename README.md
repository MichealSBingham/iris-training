# IrIs

This is the repository containing all files containing code to train IrIs


## Dependency Installation

Install the required packages using requirements.txt, make sure you are using Python 3
```bash
pip install -r requirements.txt
``` 

Note that even after installing the requirements, you may get a Library Not Found Error and have to install one more library on some machines. 


## Prepare Directories 


(1). Put the dataset root into the project folder /iris 
	- It should have a structure like so: 
				/iris
					-/ucf-crime-dataset 
						-/abuse 
							-..Videos of abuse 
							 ...
						-/theft 
							-... Videos of theft 
						/...
						/...
						/Rest of Categories...

(2) Make a new folder in the same directory of the iris repository named 'dataset' and create the following folders inside it. (Without copying the videos. This directory should be empty for now with only folders)
				/dataset 
					/test 
						/abuse 
						/theft
						/etc. (Folder names must be the same as the folder names in the crime dataset)
					/train
						/abuse 
						/theft
						/etc. (Folder names must be the same as the folder names in the crime dataset)
					/val 
						/abuse 
						/theft
						/etc. (Folder names must be the same as the folder names in the crime dataset)
 
## Split the video dataset into test/train/val sets

Run the python script split.py using the paths to the directories as arguments. Make sure you are using Pip 3. 

```bash
python split.py ucf-crime-dataset 0.2 dataset
``` 

'ucf-crime-dataset' is the local path to the ucf-crime-dataset
'dataset' is the local path to the newly created directory just made. 
'0.2' means we'll split it into 20% testing 

# Now run frame_extractor and follow the instructions  

```bash
python frame_extractor.py
``` 

Enter the path to 'dataset' and you're done

## Authors and acknowledgment

Created by Yours Truly Micheal S. Bingham 





