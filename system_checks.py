from concurrent.futures import process
from runpy import run_module
import subprocess
import os
import sys
import platform
import pip
import pkg_resources


def apt():
    subprocess.call(["sudo", "apt", "update"])
    subprocess.call(["sudo", "apt", "upgrade", "-y"])
    return "done"


def Rasp_os_ver():
    os_file = open("/etc/os-release", "r")

    for line in os_file:
        if line.__contains__("VERSION_CODENAME"):
            version = line.strip("VERSION_CODENAME=").strip('\n')
        if version != "buster":
            os_file.close()
            sys.exit("Your distro is not supported")
    os_file.close()
    return version


def platform_check():
    plat = platform.architecture()
    if (plat[0] != "32bit"):
        sys.exit("Invalid Arch")
    return plat[0]


def get_python_version():
    python_version = platform.python_version()
    if python_version < "3.7.3":
        sys.exit("Your Python Version is too low")
    return python_version

def get_python_installed_packages():
    #This line is from https://stackoverflow.com/questions/35120646/python-programmatically-running-pip-list
    x = [p.project_name for p in pkg_resources.working_set]
    for i in x:
        if i == "GitPython":
            print (i)
            return 0
        else:
            subprocess.call(["pip", 'install', '-i'])
        break