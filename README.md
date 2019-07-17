# Python Image Comparison using OpenCV

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
Final results will be outputed to 'results.csv' in the current directory