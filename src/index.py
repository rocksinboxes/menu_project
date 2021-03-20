from sys import argv
from github_repo import define_remote_repo


update_repo = define_remote_repo(argv[1], argv[2])
print(argv[1], argv[2])