from subprocess import call
from sys import exit
from platform import python_version, architecture


class system_check:
    def __init__() -> None:
        minimum_python_version = "3.7.3"
        minimum_distro_version = "buster"

    def apt_system_checks():
        call(["sudo", "apt", "update"])
        call(["sudo", "apt", "upgrade", "-y"])

    def rasp_os_ver():
        os_file = "/etc/os-release"
        with open(os_file, 'r') as f:
            data = f.read()
            data = data.splitlines()[4].split("=")[1]
            if data != system_check.minimum_distro_version:
                f.close()
                exit("Unsupported Distro")
            f.close()
        return True

    def platform_check():
        plat = architecture()
        if plat[0] != "32bit":
            exit("Invalid Arch")
        return plat[0]

    def get_python_version():
        python_version = python_version()
        if system_check.python_version < system_check.minimum_python_version:
            exit("Your Python Version is too low")
        return system_check.python_version

    def install_required_pip_packages():
        call(["pip", "install", "--upgrade" "pip",
             "systemtools", "disttools", "wheel"])
        with open('/home/pi/menu_project/requirements.txt', 'r') as f:
            for line in f:
                data = line.strip("\n").split()[0]
                call(["pip", "install", data])
                f.close()
                exit(0)
