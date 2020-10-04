"""
Create Virtual Environment for your project and automatically install requirements.
"""
import os
from subprocess import Popen
from virtualenv import cli_run

from djangular_cli.config import app_settings
from djangular_cli.config.app_settings import djangular_root_dir


class Env:
    """
    Data
    """

    def __init__(self):
        self.requirements = djangular_root_dir("dependencies/requirements.txt")
        self.choose_path = input("▸ Choose your Virtualenv path: ")
        self.name_env = input("▸ Name your Virtualenv [djangular_env]: ")


def cmd_env():
    """
    Create Virtual Environment for your project and automatically install requirements.
    [Options]:
    Choose path or use CWD to install virtual environment
    Choose a name for virtual environment
    Code readability: 'join' / 'expanduser' reused from DJANGUALR settings
    """
    data = Env()

    print("To install in current directory [Enter]: " + os.getcwd())
    choose_path = data.choose_path
    name_env = data.name_env
    venv_dir = os.path.join(os.path.expanduser(choose_path), name_env)
    cli_run([venv_dir])

    if choose_path or name_env:
        print("▸ Virtualenv path: ", str(choose_path + ": " + name_env))
    else:
        if choose_path == "":
            print("▸ Virtualenv path: ", str(os.getcwd() + ": " + name_env))

    print("▸ Activate {} with 'djangular -env activate'".format(name_env))

    activate_file = os.path.join(venv_dir, "bin", "activate_this.py")
    with open(activate_file) as f:
        code = compile(f.read(), activate_file, "exec")
        exec(code, dict(__file__=activate_file))


def cmd_django():
    """
    Start Django Project
    """
    django_executable_path = getattr(app_settings, 'DJANGO_EXECUTE', 'django-admin')
    command = [django_executable_path, 'startproject',
               input("▸ " + "Django Project Name [djng_project]: ")]
    process = Popen(
        command,
        env={'PATH': os.environ.get('PATH')},
    )
    process.wait()
    return print("▸", "New Django project created in: ", os.getcwd())


def get_django_root_path():
    """
    For later use.
    Django root path.
    :return:
    """
    return getattr(app_settings, 'DJANGO_ROOT_PATH', ".")


def cmd_angular():
    """
    Start Angular project.
    """
    ng_executable_path = getattr(app_settings, 'NG_EXECUTE', 'ng')
    command = [ng_executable_path, 'new', '--routing', '--style=scss']
    process = Popen(
        command,
        env={'PATH': os.environ.get('PATH')},
    )
    process.wait()


def get_ng_root_path():
    """
    Angular root path.
    :return:
    """
    return getattr(app_settings, 'NG_ROOT_PATH', ".")
