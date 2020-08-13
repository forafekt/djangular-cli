"""""
setup module
"""""

import setuptools

from djangular_cli.config.app_settings import djangular_root_dir, join, root

app = djangular_root_dir
here = root

__al__ = ["__version__"]

with open(join(here, 'VERSION')) as f:
    __version__ = f.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(join(here, 'MANIFEST.in')) as f:
    MANIFEST = f.read().strip()

extra_files = [
    join(here, 'VERSION'),
    join(here, 'README.md'),
    join(here, 'MANIFEST.in')
]

setuptools.setup(
    name="djangular-cli",
    version=__version__,

    include_package_data=True,
    package_data={"": extra_files},
    project_urls={
        "Bug Tracker": "https://github.com/forafekt/djangular-cli/issues",
        "Documentation": "https://github.com/forafekt/djangular-cli/tree/master/djangular_cli/docs",
        "Source Code": "https://github.com/forafekt/djangular-cli",
    },

    packages=setuptools.find_packages(),
    scripts=[
        # 'djangular_cli/generate/bin/ng',
        'djangular_cli/generate/bin/django-admin'
    ],
    entry_points={
        'console_scripts': [
            'djangular=djangular_cli:main',
        ],
    },

    author="Jonny Doyle",
    author_email="jonathan.d@programmer.net",
    license="MIT",
    description="Django / Angular project management.",
    keywords="django angular client template boilerplate git automate",
    platform="Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forafekt/djangular-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    install_requires=[
        "PyInquirer",
        "pip",
        "virtualenv",
        "setuptools",
        "django-environ",
        "distlib",
        "pyfiglet",
    ],
    python_requires='>=3.6',
)
