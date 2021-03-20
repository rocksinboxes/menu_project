
from subprocess import run
from file_download import download_file

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