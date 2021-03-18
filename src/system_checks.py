from concurrent.futures import process
from runpy import run_module
import subprocess
import os
import sys
import platform
import pip
import pkg_resources

class system_check:
    def __init__(self) -> None:
        self.minimum_python_version = "3.7.3"

    def apt():
        subprocess.call(["sudo", "apt", "update"])
        subprocess.call(["sudo", "apt", "upgrade", "-y"])
        return "done"

    def Rasp_os_ver(self):
        self.os_file = open("/etc/os-release", "r")

        for self.line in self.os_fileos_file:
            if self.line.__contains__("VERSION_CODENAME"):
                self.version = self.line.strip("VERSION_CODENAME=").strip('\n')
            if self.version != "buster":
                self.os_file.close()
            sys.exit("Your distro is not supported")
        self.os_file.close()
        return self.version

    def platform_check(self):
        self.plat = platform.architecture()
        if (self.plat[0] != "32bit"):
            sys.exit("Invalid Arch")
        return self.plat[0]

    def get_python_version(self):
        self.python_version = platform.python_version()
        if self.python_version < self.minimum_python_version:
        sys.exit("Your Python Version is too low")
        return self.python_version

    def get_python_installed_packages():
        # This line is from https://stackoverflow.com/questions/35120646/python-programmatically-running-pip-list
        self.pip_package_list = [
            self.p.project_name for self, p in pkg_resources.working_set]
        for self.inter_list in self.pip_package_list:
            if self.inter_list == "GitPython":
                print(self.inter_list)
                return 0
            else:
                subprocess.call(["pip", "install", "-i"])
            break
