# IrIs

This is the repository containing all files containing code to train IrIs


## Dependency Installation

Install the required packages using requirements.txt, make sure you are using Python 3
```bash
pip install -r requirements.txt
``` 

Note that even after installing the requirements, you may get a Library Not Found Error and have to install one more library on some machines. 

 
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

## Training 

Make sure the dataset is in the directory of the project. The name of the folder should be 'dataset'. The folder should have a structure like the following: 
	- dataset 
		\ train 
			- Abuse 
				- 1001.jpg
				- 1002.jpg 
				... 
			...
		\test 
			- Abuse 
				- 1001.jpg
				- 1002.jpg 
				... 
			...
		\val 
			- Abuse 
				- 1001.jpg
				- 1002.jpg 
				... 
			...

Now run the training file. 
```bash
python train_cnn.py
``` 

## Authors and acknowledgment

Created by Yours Truly Micheal S. Bingham 





