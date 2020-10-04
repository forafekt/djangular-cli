import os


class Utils(object):
    """
    Mixin to get commonly used directories in Djangular Commands
    """
    def get_default_app(self):
        """
        Get name of the django app that contains the site config.
        """
        return os.environ["DJANGO_SETTINGS_MODULE"].replace('.settings', '')

    def get_default_path(self):
        """
        Get name of the django app that contains the site config.
        """
        settings_module = __import__(self.get_default_app())
        return settings_module.__path__[0]

    def get_djangular_root(self):
        """
        Get the absolute path of app.
        """
        return os.getcwd()

    def get_root(self):
        """
        Get root of the project directory without having to have a entry in the settings.
        """
        default_site = self.get_default_app()
        path = self.get_default_path()
        for _ in range(len(default_site.split('.'))):
            path = os.path.dirname(path)
        return path
