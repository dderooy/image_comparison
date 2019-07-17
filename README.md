# Python Image Comparison using OpenCV

The pictures have 0.13698 similarity: 
![alt text](https://github.com/dderooy/image_comparison/blob/master/similarity_0.13698630137.jpg "comparison results")

This program consumes a csv file of image pairs and conducts a comparison using OpenCV. Similarity ranges from 0 - 1
with 0 being the same image. 

### Code Setup (using a mac): 
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
Run the project unittests. The first time they will fail since the test data is being created with image paths
specific to your system. Running this command a second time will allow all tests to pass. 
```bash
python -m unittest discover
```

### Operation (using a mac): 
Open the 'input_data.csv' file and add all picture pairs for the comparison. Once the input csv file is setup,
inside the terminal run: 
```bash
python CompareImages.py
```
Final results will be outputed to 'results.csv' in the current directory. The resutls file contains the similarity of 
each image pair, as well as the elapsed computation time in seconds for each image. 

### Packaging the application into exe
Install pyinstaller
```bash
pipenv install pyinstaller
```
This will create executable files depending on the OS being used. (since I don't have a windows machine
I can only create mac executable files)
```bash
pyinstaller -F CompareImages.py
```
The executable file will be located in the 'dist/image_comparison' folder.