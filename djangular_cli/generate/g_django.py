from virtualenv.util import subprocess

from djangular_cli.config import app_settings
from djangular_cli.config.app_settings import OSget, current_dir


def cmd_django():
    """
    Start Django Project
    """
    django_executable_path = getattr(app_settings, 'DJANGO_EXECUTABLE_PATH', 'django-admin')
    command = [django_executable_path, 'startproject',
               input("Django Project Name [dist]: ")]
    process = subprocess.Popen(
        command,
        env={'PATH': OSget('PATH')},
    )
    process.wait()
    return print("New Django project created in: ", current_dir)


def get_django_root_path():
    """
    For later use.
    Django root path.
    :return:
    """
    return getattr(app_settings, 'DJANGO_ROOT_PATH', ".")
