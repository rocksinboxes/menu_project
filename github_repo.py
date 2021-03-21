
from requests import get
from os import path
from sys import exit
from time import ctime
from dateutil.parser import parse
import default_paths
from git import Repo


class define_remote_repo():

    def __init__(self, name, repo) -> None:
        self.repo = repo
        self.name = name
        self.local_repo = Repo(
            f"{default_paths.default_paths.home_path}{self.repo}")

    def get_json_data(self):
        get_repo = f"{default_paths.default_paths.github_url}{self.name}/{self.repo}"
        r = get(get_repo)
        r_data = r.json()
        return r_data

    def clone_remote_repo(name,repo,local_repo):
        name=name
        repo=repo
        local_repo=f"/home/pi/{local_repo}"
        Repo.clone_from( f"https://github.com/{name}/{repo}.git", local_repo)

    def update_repo(self):
        self.local_repo.remotes.origin.fetch()
        self.local_repo.remotes.origin.pull()
        exit(0)

    def timezone_convert(self):
        self.local_heads = self.local_repo.head.commit
        self.local_repo_time = ctime((self.local_heads.authored_date))
        self.time_date_data_commits = get(
            f"{default_paths.default_paths.github_url}{self.name}/{self.repo}/commits")
        self.time_zone_data = self.time_date_data_commits.json()
        self.remote_repo_net_time = self.time_zone_data[0]["commit"]["author"]["date"]
        self.local_parsed_net_time = parse(
            self.remote_repo_net_time)
        self.correct_net_time = self.local_parsed_net_time.ctime()
        if self.local_repo_time != self.correct_net_time:
            self.local_repo.remotes.origin.fetch()
            self.local_repo.remotes.origin.pull()
        exit(0)
