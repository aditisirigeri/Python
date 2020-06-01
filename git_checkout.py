from github import Github
# First create a Github instance:
g = Github('53c4188af38806fba3c88ae72f1e5fc9e3f36c98')
user = g.get_user()
user.login
g = Github(base_url="https://github.com/aditisirigeri", login_or_token="53c4188af38806fba3c88ae72f1e5fc9e3f36c98")
repositories = g.search_repositories(query='language:python')
for repo in repositories:
	print(repo)
