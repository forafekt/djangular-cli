"""""
DJANGULAR reusable settings
"""""
import environ
import os

"""""
Reuse import os 
So we only have to import once
importing from here will only import the needed os attributes
"""""
current_dir = os.getcwd()
join = os.path.join
expanduser = os.path.expanduser
cmd = os.system
exists = os.path.exists
change_dir = os.chdir
OSget = os.environ.get
OSEnv = os.environ
PathDirName = os.path.dirname


"""""
DJANGULAR root directory
"""""
djangular_root_dir = (environ.Path(__file__)) - 2
root = (environ.Path(__file__)) - 3


"""""
Django settings
"""""
DJANGO_ROOT_PATH = current_dir
DJANGO_EXECUTE = djangular_root_dir("generate/bin/django-admin")

"""""
Angular settings
"""""
NG_ROOT_PATH = current_dir
NG_EXECUTE = "ng"  # djangular_root_dir("generate/bin/ng")

"""""
ENV settings
"""""
ENV_ROOT_PATH = current_dir
ENV_EXECUTE = djangular_root_dir("generate/bin")



