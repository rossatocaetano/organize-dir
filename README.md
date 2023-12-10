# Organize Directories Utility 🗂️
<p align="center">[under construction 🏗️]</p>

## About
This project was created to organize multiple files of a directory, saving time of the user

## Features
* ✅Organize directories with a script
* ✅Filter user input data
* ⚠️Organize directories with a Graphical User Interface (GUI)

This organize directories utility was developed with Python 3.10.1 version

## Instructions
In the file config.py, change the 'dir' variable value to the directory path that you want to organize as the model below
- for windows: 'dir':'C:/Users/my_user/paste-to-organize'
- for linux: 'dir':'/home/my-user/paste-to-organize'
Example:
~~~python
config = {
    'max_len' : 4,
    'dir':'/home/my-user/Downloads'
}
~~~

Note: The max_len is a value, which means the number of words that the format in the directory may have. The standart value is 4.