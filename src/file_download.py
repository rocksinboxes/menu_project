
import requests
import os
import subprocess
import tempfile


class download_file:
    def __init__(self, url) -> None:
        self.url = url
        self.urlname = self.url.rsplit('/', 1)[1]

    def download(self):
        tmp = tempfile.mktemp()
        path = tmp
        r = requests.get(self.url, stream=True)
        download = r.content
        with open(f"{tmp}", "wb") as f:
            f.write(download)
            os.chmod(f"{tmp}", 755)
            f.close()
            subprocess.call(["sudo", f"{tmp}"])
        os.remove(path)


x = download_file("https://deb.nodesource.com/setup_15.x")
x.download()
