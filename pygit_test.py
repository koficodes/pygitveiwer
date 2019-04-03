from pygit2 import Repository

repo = Repository('/home/paul/dashboard_repo/dashboard_etl/.git')
print(repo.head.shorthand)
