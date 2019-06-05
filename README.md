SnowBot-3000
===

Codebase for SnowBot-3000 interactive-friend web project

<p align="center">
  <img src='/snowbot/static/images/snowbot2.GIF' width='600px'>
</p>

What is SnowBot-3000? 
===

SnowBot-3000 is a robot made of e-waste, mostly comprised of 2012 13" Macbook Pro bottom-cases. It utilizes the OSX/macOS Speak Synthesis Manager to convert text to speech. It features a Macbook Pro as the brain, running macOS Mojave. The codebase is pure Python 3.7, the Django Web-Framework, with a little Javascript/ajax used for asychronus server requests. It is meant to run locally, with the main index page displayed on an iPad. [Click here](https://vimeo.com/339687763) to see an example of it's operation in action. 

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
In order to install SnowBot-3000, it's recommended you use a virtual environment. If you already know how to set that up, jump to the "Setting Up SnowBot-3000" section further on. 

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
source venv_snowbot/bin/activate
```
You should now see `(venv_snowbot)` on your terminal line. Congratulations — you are now ready to install **Django**!

Installing Django
===
* Download the SnowBot-3000 project, unzip, then navigate to the **snowbot3000-master** folder in **Terminal** – you should see a **requirements.txt** file contained within.
* If you're not sure how to do this, just type the following in **Terminal**:
```
cd ~/Downloads/snowbot3000-master/
```

*This project was built using Django 1.11.17, but it'll probably work with the latest version. However, it's recommended that you install this version just to be certain it works.* 

* Run the following from **Terminal**:
```
pip install -r requirements.txt
```
If no errors are present, then you've successfully installed everything you need to get SnowBot-3000 up and running. Let's do that now!

Setting Up SnowBot-3000
===

In order to get SnowBot-3000 up and running, theres a few things we need to do first. 

* From within the **snowbot3000-master** folder, navigate to the **snowbot** directory – you should see a **manage.py** file.
* If you're not sure how to do this, just type the following in **Terminal**:
```
cd ~/Downloads/snowbot3000-master/snowbot/
```
* Run the following from **Terminal**:
```
python manage.py runserver 0.0.0.0:8000
```
If everthing is setup correctly, you should see the following output:
```
Django version 1.11.17, using settings 'snowbot.settings'
Starting development server at http://0.0.0.0:8000/
```
Now you to need verify that you can actually see the interface. 
* Open up your web-browser of choice and enter the url **localhost:8000**.
* Additionally, you can enter the IP address of your computer, followed by **:8000**. ex: **192.168.1.3:8000**

You should see the iPad Kiosk interface, and be able to click the icons and hear the output. If so, you've successfully setup SnowBot-3000 – Great Job!

Visiting SnowBot-3000 from Within Your Network
===
Now that you've got SnowBot-3000 up and running, you need to be able to view it from other devices – this is the best part!
* Obtain the IP address of your computer (if you navigated to SnowBot-3000 in your browser by IP, you already have this)
* From a web-browser on a device connected to the same network as your computer, type your IP address followed by **:8000**. ex: **192.168.1.3:8000**  

You should see the same iPad Kiosk view as you did on your computer. If so, you've successfully setup SnowBot-3000 on your local network and are ready to use it – Awesome Job!!

Using Django Admin
===
One of the coolest features of SnowBot-3000 is the Django Admin panel, where you can add, delete, and update stock SnowBot-3000 phrases. As a default, the project already has a working SQLite database, so there's no need to create one. You can if you want, but the current one already has a few stock phrases that you'll lose if you delete it and start fresh. 
* From your computer (the one hosting SnowBot-3000), navigate to **localhost:8000/admin**
* The admin 'username' and 'password' can be found in **admin.py** file located in **snowbot/mainapp/admin.py**. 

Once logged in, you'll see three categories under 'MAINAPP': 'Jokes', 'Sings', 'Wisdoms'. 
Here you can add, delete, or change any of the entries.

Now you are pretty much set, and can bend SnowBot-3000 to your liking! 

A quick note: Everytime you add a phrase to any of the categories, SnowBot-3000 will speak the newest entry. After that, it goes back to selecting a random phrase everytime the corresponding icon is selected in iPad Kiosk view. The more phrases you add, the more random the selections become, so I suggest creating many entries. Have fun with SnowBot-3000, and please don't abuse it's power.

Enjoy!!
---





