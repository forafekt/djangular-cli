from djangular_cli.config.app_settings import djangular_root_dir, join, PathDirName

here = djangular_root_dir()
__all__ = ["__version__"]

with open(join(PathDirName(here), '../VERSION')) as version_file:
    __version__ = version_file.read().strip()
