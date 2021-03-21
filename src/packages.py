
from subprocess import run
from file_download import download_file
from system_checks import system_check

class nodejs:
    def __init__(self) -> None:
        self.name = "nodejs"
        self.download = download_file("https://deb.nodesource.com/setup_15.x")

    def nodejs_install(self):
        self.download.download_installer()
        run(["sudo", "apt", "install", self.name, "-y"])

    def nodejs_update(self):
        system_check.apt_system_checks()
       