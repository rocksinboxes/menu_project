
from gettext import install
from sys import argv, exit
from subprocess import call, run
from file_download import download_file
import system_checks
import locale
locale.setlocale(locale.LC_ALL, '')


class nodejs:
    def __init__(self) -> None:
        self.name = "nodejs"
        self.download = download_file("https://deb.nodesource.com/setup_15.x")

    def nodejs_install(self):
        self.download.download_installer()
        run(["sudo", "apt", "install", self.name, "-y"])

    def nodejs_update(self):
        run(["sudo", "apt", "update"])
        run(["sudo", "apt", "upgrade"])
        return 0


nodejs = nodejs()
try:

    len (argv[2]) == 0
        
except:
        exit("You didn't enter any parameters")

try:
    if argv[1] == "update" or argv[1] == "install":
        for val in argv[2:]:
            function = f"{val}.{val}_{argv[1]}()"
            eval(function)
except:
    exit("Invalid Entry. Please Try again")
