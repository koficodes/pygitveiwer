from pygit2 import Repository, discover_repository
import os

path = '/home/paul/dashboard_repo/'

# print(repo.head.shorthand)
for info in os.listdir(path):
    discover_repository(path+info)
