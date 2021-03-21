from gettext import install
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
        os_file = "/etc/os-release"
        with open(os_file, 'r') as f:
            data = f.read()
            data = data.splitlines()[4].split("=")[1]
            if data != self.minimum_distro_version:
                f.close()
                exit("Unsupported Distro")
            f.close()
        return True

    def platform_check():
        plat = architecture()
        if plat[0] != "32bit":
            exit("Invalid Arch")
        return plat[0]

    def get_python_version(self):
        self.python_version = python_version()
        if self.python_version < self.minimum_python_version:
            exit("Your Python Version is too low")
        return self.python_version

    def install_required_pip_packages():
        run (["python", "-m", "install", "--upgrade", "pip", "systemtools", "disttools"])
        with open('/home/pi/menu_project/requirements.txt', 'r') as f:
            for line in f:
                data = line.strip("\n").split()[0]
                run(["pip", "install", data])
                f.close()
