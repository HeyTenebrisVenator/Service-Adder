from colorama import Fore
import os
from tkinter import *




def systemctl(path, service_name):
    service_template = f"""[Unit]
Description=ROT13 demo service

[Service]
Type=simple
ExecStart=/usr/bin/python3 {path}

[Install]
WantedBy=default.target
"""
    open("/usr/lib/systemd/system/" + service_name + ".service", "w").write(service_template)
    q1 = input("Start Service? Y/n\n  >> ").lower()
    if q1 == "y":
        os.system(f"sudo systemctl start {service_name}")
    q2 = input("Enable Service when the computer boot? Y/n\n  >> ").lower()
    if q2 == "y":
        os.system(f"sudo systemctl enable {service_name}")


def textbox():
    window = Tk()
    white = "white"
    black = "black"

    window["bg"] = white
    window.geometry("500x500+50+50")

    def collect_data():
        content = text.get('1.0', 'end-1c')  # get text, remove trailing newline
        file_path = os.path.join(home_dir, NameService)
        with open(file_path, 'w') as f:
            f.write(content)
        window.destroy()

    framepri = LabelFrame(window, bg=black)
    text = Text(window, bg=white, fg=black)
    collect = Button(window, bg=black, text="Send", fg=white, command=collect_data)

    framepri.pack(anchor=NW)
    text.pack(anchor=NW)
    collect.pack(anchor=NW)

    window.mainloop()

home_dir = os.path.expanduser("~") + "/.service_adder"
if not os.path.exists(home_dir):
    print("~/.service_adder doesn't exist, creating one...")
    try:
        os.mkdir(home_dir)
    except Exception as e:
        print("ERROR GENERATING DIRECTORY:", e)
        quit()


NameService = input("Name of the Service  >>  ")
try:
    open(home_dir + "/" + NameService, 'r').read()
except:
    print("File don't existe, creating one...")
    open(home_dir + "/" + NameService, 'w').write(" ")

print("Please, write the code in the textbox, and then press send")
textbox()
systemctl(home_dir + "/" + NameService, NameService)