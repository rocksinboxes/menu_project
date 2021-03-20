from requests import get
from os import remove, chmod
from subprocess import run
from tempfile import mktemp
import default_paths


class download_file:
    def __init__(self, url) -> None:
        self.url = url
        self.urlname = self.url.rsplit('/', 1)[1]

    def download_installer(self):
        tmp = mktemp()
        path = tmp
        r = get(self.url, stream=True)
        download = r.content
        with open(f"{tmp}", "wb") as f:
            f.write(download)
            chmod(f"{tmp}", 755)
            f.close()
        run(["sudo", f"{tmp}"])
        remove(path)


class install_deb_file:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.apt_install = run(
            ["sudo", "apt", "install", f"{default_paths.default_paths.home_path}Downloads/{self.filename}"], capture_output=True)


