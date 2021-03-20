from os import getlogin


class default_paths():
    login = getlogin()
    home_path = f"/home/{login}/"
    github_url = "https://api.github.com/repos/"
