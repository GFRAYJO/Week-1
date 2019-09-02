# KThreading through Different Time Sequences 

These instructions will help you run this project on your local machine for development and testing.  This program allows you as the developer or user to know how to perform a multi-threading action while calculating the area and circumference of a circle through the use the time sequence.  

kthread is a library in Python that provides the ability to actively terminate(), kill(), join(), and/or exit() an ongoing running thread, it is an extension to the well-known thread library. 

Time is a library within Python that provides the conversion of time in its proper format when ran in conjunction with mulitple threads at different times.

Colorama is a library that allows text and results to display in the terminal in color.

## Installation and Necessary Software

It is important to have access to the appropriate software for running this project.  
- Install Python 3.0 and above installed on your machine (Python 3.0 or above comes equipped with pip which is necessary for this project ) 
- Install Visual Studio Code (add the Pylint extension)
- Ensure you have pip installed if not on Python 3.0 or above (https://packaging.python.org/tutorials/installing-packages/).
- You will need to install the pipenv (pip virutal environment within the project)
- To install KThread use the package manager [pip] to install kthread (https://pypi.org/)
    - pip install kthread
- To install Colorama use the package manager [pip] to install colorama (https://pypi.org/)
    - pip install colorama
- The executable file (KThreading.exe) was compiled using pyinstaller which allows the program to run on any windows machine.

## Usage Example

import kthread
import time
from colorama import init, Back, Fore

init()


When ready to run this project, simply double click on the KThreading.exe file and the application will begin to run.
 
