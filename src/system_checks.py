from subprocess import run
from sys import exit
from platform import python_version, architecture


class system_check:
    def __init__(self) -> None:
        self.minimum_python_version = "3.7.3"
        self.minimum_distro_version = "buster"

    def apt_system_checks():
        run(["sudo", "apt", "update"])
        run(
            ["sudo", "apt", "upgrade", "-y"])
 

    def rasp_os_ver(self):
        self.os_file = open("/etc/os-release", "r")

        for self.line in self.os_file:
            if self.line.__contains__("VERSION_CODENAME="):
                self.version = self.line.strip("VERSION_CODENAME=").strip('\n')
            if self.version != self.minimum_distro_version:
                self.os_file.close()
                exit("Your distro is not supported")
        self.os_file.close()
        return self.version

    def platform_check(self):
        self.plat = architecture()
        if (self.plat[0] != "32bit"):
            exit("Invalid Arch")
        return self.plat[0]

    def get_python_version(self):
        self.python_version = python_version()
        if self.python_version < self.minimum_python_version:
            exit("Your Python Version is too low")
        return self.python_version
    def install_required_pip_packages():
        
        with open('/home/pi/menu_project/requirements.txt', 'r') as f:
            for line in f:
                data=line.strip("\n").split()[0]
                run(["pip", "install", data])
                f.close() 