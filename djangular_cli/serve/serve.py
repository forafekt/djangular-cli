from subprocess import Popen

from django.conf import settings

from djangular_cli.config import app_settings
from djangular_cli.config.app_settings import OSget


def get_project_static_root():
    """
    Find django static root
    """
    static_path = getattr(settings, "STATIC_ROOT", "static")
    return static_path


class AngularBuild:
    """
    Build data
    """
    command = "ng"
    prefix_prod = "--prod --output-path"
    prefix_hash = "--output-hashing none"
    path = get_project_static_root

    def __init__(self):
        self.command = None
        self.prefix_prod = str
        self.prefix_hash = str
        self.path = str


def build_angular():
    """
    Build Angular project to Django static and organise.
    """
    build = AngularBuild()
    command = build.command
    prefix_prod = build.prefix_prod
    prefix_hash = build.prefix_hash
    path = build.path
    ng_execute = command
    command = [ng_execute, prefix_prod, path, prefix_hash]
    process = Popen(
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
