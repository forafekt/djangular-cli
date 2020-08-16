import time

from djangular_cli.config.app_settings import cmd
from djangular_cli.generate.create import Env as getEnv


def activate_env():
    """
    Activate Virtualenv with 'djangular -env activate'
    """
    data = getEnv()
    try:
        venv_path = data.choose_path
        venv_name = data.name_env
        if venv_path:
            if venv_path[-1] != '/':
                venv_path += '/'
        else:
            venv_path = ''

            fe = ".sh"  # File extension
            input_to_sh = ("#!/bin/bash\n"  # File data
                           ". {}{}/bin/activate; exec /usr/bin/env bash")
            # Create file with given data
            with open('{}/bin/activate_{}{}'.format(venv_name, venv_name, fe), 'w+') as createfile:
                createfile.write(input_to_sh.format(venv_path, venv_name))
            # Find file to execute
            with open('{}/bin/activate_{}{}'.format(venv_name, venv_name, fe), 'r') as file:
                filedata = file.read()
                # Execute script
                try:
                    print("▸ Attempting to activate: " + venv_name)
                    time.sleep(2)
                    print("▸ ", venv_name + " Activated.")
                    cmd(filedata)
                except exit as End:
                    End("There was an error activating the {}.".format(venv_name))
    except EnvironmentError:
        print("Failure! Retry...")
    else:
        pass
