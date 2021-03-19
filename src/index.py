import sys, github_repo

class parse_args:
    def __init__(self) -> None:
        self.cli_args = sys.argv



x=github_repo.Define_Remote_Repo('botspot','pi-apps')


print (x.update_repo())