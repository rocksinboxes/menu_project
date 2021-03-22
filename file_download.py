from requests import get
from os import remove, chmod
from subprocess import run,call
import tempfile 
import default_paths


class download_file():

    def download_installer(url):
        download=url
        r= get(download, stream=True)
        data=r.content
        with open("/home/pi/test.sh", "wb") as f:
            f.write(data)
            chmod ('/home/pi/test.sh',755)
            f.close()
    

     
       
    
        
        

        

class install_deb_file:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.apt_install = run(
            ["sudo", "apt", "install", f"{default_paths.default_paths.home_path}Downloads/{self.filename}"])