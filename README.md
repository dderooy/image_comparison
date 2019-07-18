# Python Image Comparison using OpenCV

The pictures have 0.13698 similarity: 
![alt text](https://github.com/dderooy/image_comparison/blob/master/similarity_0.13698630137.jpg "comparison results")

This program consumes a csv file of image pairs and conducts a comparison using OpenCV. Similarity ranges from 0 - 1
with 0 being the same image. 

### Code Workspace Setup (using a mac): 
(**using python 2.7.14**)

After cloning the repository and opening the directory in a terminal, run the below commands

Pipenv: is used to control the project dependencies and python environments
```bash
sudo pip install pipenv
```
Check to see if pipenv is installed correctly
```bash
pipenv
```
Install project dependencies using python 2
```bash
pipenv install --two
```
Run the python environment
```bash
pipenv shell
```
### Unit Tests
Run the project unittests. The first time they will fail since the test data is being created with image paths
specific to your system. Running this command a second time will allow all tests to pass. 
```bash
python -m unittest discover
```

### Operation (using a mac): 
Run the command and follow the instructions: 
```bash
python CompareImages.py
```

The program will ask for the path of an input and output file and build a results file. The resutls file contains
the similarity of each image pair, as well as the elapsed computation time in seconds for each image. 

### Creating executable files for Mac and Windows
Install pyinstaller
```bash
sudo pip install pyinstaller
```
This will create an executable file depending on the OS being used. (since I don't have a windows machine
I can only create mac executable files)
```bash
pyinstaller CompareImages.spec
```
The executable file will be located in the 'dist/image_comparison/' folder.


