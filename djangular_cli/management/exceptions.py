"""""
Client error handler.
"""""


class DjangularExeption(Exception):
    """""
    Exceptions
    """""
    pass


class ArgDoesNotExist(DjangularExeption):
    """""
    Arg doesn't not exist
    """""

    def _raise(self):
        for var in self.args:
            if not var == str:
                raise ArgDoesNotExist


