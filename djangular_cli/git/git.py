"""
Simple Git clone tool
Code readability: cmd, exists, current_dir, change_dir reused from DJANGULAR settings
"""
import shutil

from djangular_cli.terminal import prompt
from distlib._backport import shutil  # noqa F405

from djangular_cli.config.app_settings import cmd, exists, current_dir
from djangular_cli.management.prompts import prompt_overwrite


class Repo:
    """
    Gather repository data to clone.
    """

    def __init__(self):
        self.git_url = "https://" + input("▸ [github.com][other]: https://")
        self.user = input("▸ Author: ")
        self.package_name = input("▸ Package name: ")
        self.result = "{}/{}/{}.git".format(self.git_url, self.user, self.package_name)
        self.to_clone = "git clone "
        self.command = self.to_clone + self.result
        self.absolute_path = current_dir + "/" + self.package_name


def djangular_boilerplate():
    """
    Clone any repository into your project.
    """
    git = Repo()
    path = git.absolute_path
    package_name = git.package_name
    clone = git.command
    if not exists(path):
        cmd(clone)
    elif exists(path):
        ow = prompt(prompt_overwrite)
        if ow.get("overwrite", True):
            shutil.rmtree(package_name)
            cmd(clone)
        else:
            exit("You have chosen not to overwrite. Session ended.")
