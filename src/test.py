
from subprocess import run
from sys import exit

def install_required_pip_packages():
    with open('/home/pi/menu_project/requirements.txt', 'r') as f:
        for line in f:
            data=line.strip("\n").split()[0]
            run(["pip", "install", data])
            f.close() 
