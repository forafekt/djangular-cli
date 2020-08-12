from virtualenv.util import subprocess

from djangular_cli.config import app_settings
from djangular_cli.config.app_settings import OSget, NG_EXECUTE


def cmd_angular():
    """
    Start Angular project.
    """
    command = [NG_EXECUTE, 'new', '--routing', '--style=scss']
    process = subprocess.Popen(
        command,
        env={'PATH': OSget('PATH')},
    )
    process.wait()


def get_ng_root_path():
    """
    Angular root path.
    :return:
    """
    return getattr(app_settings, 'NG_ROOT_PATH', ".")
