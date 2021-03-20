from subprocess import run
from sys import exit
from platform import python_version, architecture
from pkg_resources import working_set

class system_check:
    def __init__(self) -> None:
        self.minimum_python_version = "3.7.3"
        self.minimum_distro_version="buster"

    def apt(self):
        self.apt_update=run(["sudo", "apt", "update"],capture_output=True)
        self.apt_upgrade=run(["sudo", "apt", "upgrade", "-y"],capture_output=True)
        return f"Your apt update return code is {self.apt_update.returncode} and your apt upgrade is {self.apt_update.returncode}"

    def rasp_os_ver(self):
        self.os_file = open("/etc/os-release", "r")

        for self.line in self.os_file:
            if self.line.__contains__("VERSION_CODENAME="):
                self.version = self.line.strip("VERSION_CODENAME=").strip('\n')
            if self.version != self.minimum_distro_version:
                self.os_file.close()
                exit( "Your distro is not supported")
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

    def get_python_installed_packages(self):
        # This line is from https://stackoverflow.com/questions/35120646/python-programmatically-running-pip-list
        self.pip_package_list = [
            self.p.project_name for self.p in working_set]
        for self.inter_list in self.pip_package_list:
            if self.inter_list == "GitPython":
                print(self.inter_list)
                return 0
            else:
                run(["pip", "install", "-i"])
                break
