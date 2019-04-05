import os
from pygit2 import Repository, discover_repository, GitError
import click


def list_dir_repositories(path):
    path = os.path.join(path, '')
    repositories = [discover_repository(path+dir_name)
                    for dir_name in os.listdir(path)]

    return [repo for repo in repositories if repo is not None]


def get_current_branch_name(repo_path):
    repo = Repository(repo_path)
    try:
        return repo.head.shorthand
    except GitError:
        return "Not Found"


@click.command()
@click.argument('path', default='.', metavar='The directory path of git repositories')
def display_git_branches(path):
    if os.path.exists(path) and os.path.isdir(path):
        print({get_current_branch_name(repo_path): repo_path
               for repo_path in list_dir_repositories(path)})


if __name__ == "__main__":
    display_git_branches()
