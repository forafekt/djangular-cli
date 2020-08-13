"""
Create Virtual Environment for your project and automatically install requirements.
"""
import pip # noqa F405
from virtualenv import cli_run

from djangular_cli.config.app_settings import \
    djangular_root_dir, \
    current_dir, \
    join, \
    expanduser


def cmd_env():
    """
    Create Virtual Environment for your project and automatically install requirements.
    [Options]:
    Choose path or use CWD to install virtual environment
    Choose a name for virtual environment
    Code readability: 'join' / 'expanduser' reused from DJANGUALR settings
    """
    # Create, choose path/name and activate the virtual environment
    print("Press Enter to install in current directory: " + current_dir)
    choose_path = input("▸ "+"Choose your Virtualenv path: ")
    name_env = input("▸ "+"Name your Virtualenv [djangular_env]: ")
    venv_dir = join(expanduser(choose_path), name_env)
    cli_run([venv_dir])
    if choose_path or name_env:
        print("▸", "Virtualenv path: ", str(choose_path + ": " + name_env))
    else:
        if choose_path == "":
            print("▸", "Virtualenv path: ", str(current_dir + ": " + name_env))

    activate_file = join(venv_dir, "bin", "activate_this.py")
    with open(activate_file) as f:
        code = compile(f.read(), activate_file, "exec")
        exec(code, dict(__file__=activate_file))

    # Automatically install project requirements
    requirements = djangular_root_dir("dependencies/requires.txt")
    if name_env:
        pip.main(["install", "--prefix", venv_dir, "-r", requirements])
