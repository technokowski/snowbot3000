SnowBot-3000
===

Codebase for SnowBot-3000 interactive-friend web project

<p align="center">
  <img src='/snowbot/static/images/snowbot2.GIF' width='600px'>
</p>

What is SnowBot-3000? 
===

SnowBot-3000 is a robot made of e-waste, mostly comprised of 2012 13" Macbook Pro bottom-cases. It utilizes the OSX/macOS Speak Synthesis Manager to convert text to speech. It features a Macbook Pro as the brain, running macOS Mojave. The codebase is pure Python 3.7, the Django Web-Framework, with a little Javascript/ajax used for asychronus server requests. It is meant to run locally, with the main index page displayed on an iPad. 

It shreds paper (snow), but this project focuses on the code (brain). It has been featured at several K-8 STEM school sites, where students had the ability to interact with it. SnowBot-3000 is your friend; beyond that, it's a passion project.

iPad Kiosk View
====
Each of the five pictures were created on an iPad Pro 12.9", and respond when touched, making SnowBot-3000 talk. The 'input' field takes the person's name and repeats it back — Much interactive!

<p align="center">
  <img src='/snowbot/static/images/index.png' width='700px'>
</p>
          
Prerequisites
====
Currently this is specific to Mac OSX/macOS only.
```
Python 3.7.3
Django==1.11.17
pytz==2019.1
```
That's it! Every browser available has been tested. 

Installing python3
===
In order to install SnowBot-3000, it's recommended you use a virtual environment. If you already know how to set that up, jump to the "Installing SnowBot-3000" section further on. 

* First thing is to make sure you have the [latest Python installation](https://www.python.org/), which is currently 3.7.3.
* Run the package and follow the steps to complete the installation.
* Once finished, open **Terminal** and run:
```
python3 --version
```
This should produce your current python3 version. Verify that it's at least:
```
Python 3.7.3
```
Installing pip3
===
* Securely download the get-pip.py file from this [link](https://pip.pypa.io/en/stable/installing/)
* From the directory where you downloaded the file, run the following command in Terminal:
```
python3 get-pip.py
```
If all goes well, verify the installation of **pip3** by running the following in Terminal:
```
which pip3
```
This should return the install location of **pip3**. You are now ready to setup a virtual environment.

Creating a Virtual Environment
===
Creation of [virtual environments](https://docs.python.org/3/library/venv.html#venv-def) is done by executing the command `venv`
```
python3 -m venv venv_snowbot
```
* You can name your `venv` anything you like; `venv_snowbot` is just a suggestion

This creates a `venv` in your current working directory. Next you need to activate by running:
```
source venv/bin/activate
```
You should now see `(venv_snowbot)` on your terminal line. Congratulations — you are now ready to install **Django**!



