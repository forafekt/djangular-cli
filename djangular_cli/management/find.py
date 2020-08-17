import subprocess
import sys
import time
from djangular_cli.config.app_settings import OSEnv, djangular_root_dir
from djangular_cli.generate.create import cmd_env


def is_venv():
    """
    Check for env
    :return:
    """
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def check_env():
    """
    Module Check
    """
    if is_venv():
        print('Checking for Virtualenv...')
        time.sleep(2)
        print('Virtualenv exists... Continuing setup.')
    else:
        print('No Virtualenv...\n'
              'Please setup Virtualenv to install modules.')
        time.sleep(2)
        try:
            cmd_env()
        except:
            exit("Finishing setup...")


def check_modules():
    """
    Module Check
    """
    check_env()
    if is_venv():
        venv_dir = OSEnv["VIRTUAL_ENV"]
        requirements = djangular_root_dir("dependencies/django.txt")
        modules = "Django"
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        print("▸", "Checking if requirements are installed...\n")
        time.sleep(5)
        if modules in installed_packages:
            print(modules, "is installed. Please continue to enter your project name..\n")
        else:
            print("▸", modules, "not installed...\n"
                                "=> Installing {} ...".format(modules))
            time.sleep(5)
            try:
                process = subprocess.Popen(["pip", "install", "--prefix", venv_dir, "-r", requirements])
                process.wait()
            except:
                print("▸ ...Using 'pip3'")
                process = subprocess.Popen(["pip3", "install", "--prefix", venv_dir, "-r", requirements])
                process.wait()
