from codecs import replace_errors
import os
class default_paths():
    login=os.getlogin()
    home_path=f"/home/{login}/"
    github_url= "https://api.github.com/repos/"

