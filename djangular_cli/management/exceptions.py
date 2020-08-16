"""""
Client error handler.
"""""


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
            raise ArgDoesNotExist(hint)


class ReqModuleNotExist(DjangularException):
    """
    Missing module exception
    """
    def __init__(self, module):
        if self.args is ReqModuleNotExist:
            raise ReqModuleNotExist(module)


