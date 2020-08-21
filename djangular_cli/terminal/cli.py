"""""
Main Client.
"""""
from __future__ import print_function, unicode_literals

from djangular_cli.terminal.prompt import prompt
from djangular_cli.config.style.color_style import style
from djangular_cli.config.style.widget import widget
from djangular_cli.generate.create import cmd_angular, cmd_env, cmd_django
from djangular_cli.git.git import djangular_boilerplate
from djangular_cli.management.find import check_modules


def client():
    """""
    Djangular Client Wrapper
    """""
    widget()

    venv = [
        {
            'type': 'confirm',
            'name': 'CreateVirtualEnvironment',
            'message': 'Create Virtual Environment',
            'when': lambda answers: answers.get('CreateVirtualEnvironment', bool)
        },
    ]
    boilerplate = [
        {
            'type': 'confirm',
            'name': 'DjangularBoilerplate',
            'message': 'Would you like to use a Djangular Boilerplate?',
            'when': lambda answers: answers.get('DjangularBoilerplate', bool)
        },
    ]
    django = [
        {
            'type': 'confirm',
            'name': 'CreateDjangoProject',
            'message': 'Create Django Project',
            'when': lambda answers: answers.get('CreateDjangoProject', bool)
        },
    ]
    angular = [
        {
            'type': 'confirm',
            'name': 'CreateAngularProject',
            'message': 'Create Angular Project',
            'when': lambda answers: answers.get('CreateAngularProject', bool)
        },
    ]

    _venv = prompt(venv, style=style)
    _boilerplate = prompt(boilerplate, style=style)

    try:
        if _venv.get('CreateVirtualEnvironment', True):
            cmd_env()
        else:
            pass

        if _boilerplate.get('DjangularBoilerplate', True):
            djangular_boilerplate()
        else:
            _django = prompt(django, style=style)
            _angular = prompt(angular, style=style)

            if _django.get('CreateDjangoProject', True):
                check_modules()
                cmd_django()
            else:
                pass

            if _angular.get('CreateAngularProject', True):
                cmd_angular()
            else:
                pass
    except KeyboardInterrupt:
        print("\n => You have force cancelled the session.\n")

        exit("Thank You for using Djangular.  Please visit https://djangular.com")


if __name__ == '__main__':
    client()
