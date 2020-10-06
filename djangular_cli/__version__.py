import os
from djangular_cli.config.app_settings import djangular_root_dir

here = djangular_root_dir()
__all__ = ["__version__"]

with open(os.path.join(os.path.dirname(here), '../VERSION')) as version_file:
    __version__ = version_file.read().strip()
