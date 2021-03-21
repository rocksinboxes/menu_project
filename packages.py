
from subprocess import run
from file_download import download_file
from system_checks import system_check
import github_repo


class nodejs:
        

    def nodejs_install(self):
        self.name=name
        self.name = "nodejs"
        self.download = download_file("https://deb.nodesource.com/setup_15.x")
        self.download.download_installer()
        run(["sudo", "apt", "install", name, "-y"])

    def nodejs_update():
        system_check.apt_system_checks()

class asdf:
    name='asdf-vm'
    repo ='asdf'
    local_repo=".asdfbv"

    def asdf_install():
        github_repo.define_remote_repo.clone_remote_repo(asdf.name,asdf.repo,asdf.local_repo)


test=asdf
test.asdf_install()

