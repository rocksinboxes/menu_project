
import requests
import git
import os
import sys
import time
import dateutil.parser
import default_paths


class define_Remote_Repo():
    
    def __init__(self, name, repo) -> None:
        self.repo=repo
        self.name=name
        self.local_repo = git.Repo(f"{default_paths.default_paths.home_path}{self.repo}") 
        
    def get_json_data(self):
        get_repo = f"{default_paths.default_paths.github_url}{self.name}/{self.repo}"
        r = requests.get(get_repo)
        r_data = r.json()
        return r_data

        
    def clone_remote_repo(self):
        if os.path.exists(f"{default_paths.default_paths.home_path}{self.repo}") == True:
            sys.exit("Exists")
        elif len(os.path.exists(self.repo)) < 0:
            git.Repo.clone_from(f"{default_paths.default_paths.github_url}.git", self.name)
        else:
            sys.exit("Nothing to do")

    def update_repo(self):
        self.local_repo.remotes.origin.fetch()
        self.local_repo.remotes.origin.pull()
        return "Done"

    def timezone_convert(self):
        self.local_heads = self.local_repo.head.commit
        self.local_repo_time = time.ctime((self.local_heads.authored_date))
        self.time_date_data_commits = requests.get(
            f"{default_paths.default_paths.github_url}{self.name}/{self.repo}/commits")
        self.time_zone_data = self.time_date_data_commits.json()
        self.remote_repo_net_time = self.time_zone_data[0]["commit"]["author"]["date"]
        self.local_parsed_net_time = dateutil.parser.parse(
            self.remote_repo_net_time)
        self.correct_net_time = self.local_parsed_net_time.ctime()
        if self.local_repo_time != self.correct_net_time:
            return "This thing works!"
