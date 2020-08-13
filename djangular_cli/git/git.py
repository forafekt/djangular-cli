"""
Simple Git clone tool
Code readability: cmd, exists, current_dir, change_dir reused from DJANGULAR settings
"""
import shutil

from PyInquirer import prompt
from distlib._backport import shutil  # noqa F405

from djangular_cli.config.app_settings import cmd, exists, current_dir, change_dir


def confirm(overwrite):
    """
    Confirm
    :param overwrite:
    :return:
    """
    return not overwrite["overwrite"]


prompt_overwrite = [
    {
        'type': 'confirm',
        'name': 'overwrite',
        'message': 'Path already exists! Do you want to overwrite?',
        'when': lambda overwrite: overwrite.get('overwrite', bool)
    }
]


def djangular_boilerplate():
    """
    Clones the passed repo to my staging dir
    """

    git_url = "https://" + input("▸ "+"[github.com][other]: ")
    user = input("▸ "+"Author: ")
    package_name = input("▸ "+"Package name: ")

    result = git_url + "/" + user + "/" + package_name + ".git"

    # Temp method
    space = " "
    clone = "git" + space + "clone" + space

    path = current_dir

    if exists(path):
        ow = prompt(prompt_overwrite)
        if ow.get("overwrite", True):
            if path:
                shutil.rmtree(package_name)
                cmd(clone + result)
            else:
                change_dir(path)
                cmd(clone + result)
