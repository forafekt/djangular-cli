"""""
Client error handler.
"""""
from djangular_cli.management.find import check_modules


class DjangularException(Exception):
    """""
    Exceptions
    """""
    pass


class ArgDoesNotExist(DjangularException):
    """""
    Arg doesn't not exist
    """""

    def __init__(self, hint) -> None:
        if self.args is ArgDoesNotExist:
            raise hint
        return print("\n\n Argument does not exist. Did you mean => %s" % hint)


class ReqModuleNotExist(DjangularException):
    """
    Missing module exception
    """
    def __init__(self, module):
        if self.args is ReqModuleNotExist:
            raise module
        return print("Module %s not found: " % module)


