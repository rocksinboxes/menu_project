from requests import get
from os import remove, chmod, close, fchmod, path, unlink, umask, stat, write, remove
from subprocess import call, call
import tempfile
import default_paths

print()


class download_file():

    def download_installer(url):
        download = url
        r = get(download, stream=True)
        data = r.content
        temp_fd, temp_name = tempfile.mkstemp(
            dir="/tmp", prefix='install-', suffix=".sh")  
        write(temp_fd, r.content)
        close(temp_fd)
        chmod(temp_name, 0o755)
        call(["sudo", temp_name])
        remove(temp_name)


class install_deb_file:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.apt_install = call(
            ["sudo", "apt", "install",
             f"{default_paths.default_paths.home_path}Downloads/{self.filename}"])
