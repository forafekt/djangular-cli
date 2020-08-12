from virtualenv.util import subprocess

from djangular_cli.config import app_settings
from djangular_cli.config.app_settings import OSget


def build_angular():
    """
    Start Angular project.
    """
    ng_executable_path = getattr(app_settings, 'NG_EXECUTABLE_PATH', 'ng build')
    command = [ng_executable_path, '--prod', '--output-path', '{}'.format(ng_executable_path), '--output-hashing none']
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
