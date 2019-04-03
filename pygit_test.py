from pygit2 import Repository, discover_repository
import os

path = '/home/paul/dashboard_repo/'

# print(repo.head.shorthand)


def list_dir_repositories(path):
    repositories = [discover_repository(path+dir_name)
                    for dir_name in os.listdir(path)]

    return [repo for repo in repositories if repo is not None]


print(list_dir_repositories(path))
