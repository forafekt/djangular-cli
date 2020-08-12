import setuptools
import pkg_resources

from djangular_cli.config.app_settings import djangular_root_dir, join, PathDirName, root

app = djangular_root_dir
here = root

with open("README.md", "r") as fh:
    long_description = fh.read()

__all__ = ["__version__"]

with open(join(here, 'VERSION')) as f:
    __version__ = f.read().strip()

with open(join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

extra_files = [
    join(here, 'requirements.txt'),
    join(here, 'VERSION'),
    join(here, 'README.md')
]

setuptools.setup(
    name="djangular-cli",
    version=__version__,

    include_package_data=True,
    package_data={"": extra_files},
    project_urls={
        "Bug Tracker": "https://github.com/forafekt/djangular-cli/issues",
        "Documentation": "https://github.com/forafekt/djangular-cli/doc",
        "Source Code": "https://github.com/forafekt/djangular-cli",
    },
    install_requires=required,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'djangular=djangular_cli:main',
        ],
    },

    author="Jonny Doyle",
    author_email="jonathan.d@programmer.net",
    description="Django / Angular project management.",
    keywords="django angular client template boilerplate git automate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forafekt/djangular-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
