# Service-Adder
Service Adder is a automatic system that allow you to run an python script as a service. This script works with systemctl

```
   _____                 _                      _     _          
  / ____|               (_)            /\      | |   | |          
 | (___   ___ _ ____   ___  ___ ___   /  \   __| | __| | ___ _ __ 
  \___ \ / _ \ '__\ \ / / |/ __/ _ \ / /\ \ / _` |/ _` |/ _ \ '__|
  ____) |  __/ |   \ V /| | (_|  __// ____ \ (_| | (_| |  __/ |   
 |_____/ \___|_|    \_/ |_|\___\___/_/    \_\__,_|\__,_|\___|_|
```   
                                                                  
                                                              

# HOW IT WORKS?
The script works creating an file in the directory */usr/lib/systemd/system*

After the creation of the file, the script will use the command *SYSTEMCTL* to turn it on, or off.

With this script, you have the power to run a script when you turn on the computer

# HOW TO INSTALL

First, you need to download the repository on your computer

So, you can run the command

```sudo git clone https://github.com/HeyTenebrisVenator/Service-Adder.git```

After that, you need to install the libraries required by the code

So, to install it, you can run the command:

```sudo pip install -r requirements.txt```

After that, you can run the script normally with the command:

```sudo python3 ServiceAdder.py```

!REMEMBER TO RUN IT AS A SUDO!

# HOW TO SET A NEW SERVICE

To add a new service, you need to run the script with the command above

When you run it as a first time, a directory will be created: *~/.service_adder*

In this file, your python commands will be saved and runned after the configuration

And then you need to put the name of the service

# WARNING!  BE SURE TO NOT PUT AN ALREADY EXISTING FILE NAME, OR ELSE IT'LL BE REWRITED, AND IT CAN BREAK THE OPERATION SYSTEM

After that, a window will appear in the display. This window is made with the tkinter, that will be installed after you run the requirements.txt

In this window, you will notice that there is a textbox, and there you will put all the python script

After pressing send, the window will be closed.

![Image1](https://github.com/user-attachments/assets/dc7c7f26-003f-4394-826a-76b4645557bc)

