
from subprocess import run
from file_download import download_file
from system_checks import system_check
import github_repo


class nodejs:
    name = "nodejs"
    url = "https://deb.nodesource.com/setup_15.x"

    def nodejs_install():
        download_file.download_installer(nodejs.url)
    #run(["sudo", "apt", "install", name, "-y"])

    def nodejs_update():
        system_check.apt_system_checks()


class asdf:
    name = 'asdf-vm'
    repo = 'asdf'
    local_repo = ".asdf"

    def asdf_install():
        github_repo.define_remote_repo.clone_remote_repo(
            asdf.name, asdf.repo, asdf.local_repo)


n = nodejs
n.nodejs_install()
