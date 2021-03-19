import sys
import github_repo


update_repo = github_repo.Define_Remote_Repo(sys.argv[1], sys.argv[2])

data = update_repo.get_json_data()
print(data["name"])