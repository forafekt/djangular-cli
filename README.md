![PyPI - License](https://img.shields.io/pypi/l/djangular-cli)
![GitHub contributors](https://img.shields.io/github/contributors/forafekt/djangular-cli)
![GitHub last commit](https://img.shields.io/github/last-commit/forafekt/djangular-cli)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/forafekt/djangular-cli)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/forafekt/djangular-cli)
![PyPI - Downloads](https://img.shields.io/pypi/dm/djangular-cli)

# DJANGULAR-CLI

DJANGULAR-CLI aim to bring DJANGO and ANGULAR together with ease.  
This is for developers that intend on using Django as a back-end to their Angular app.
The methodology to using this client is to build a complete front-env application in angular and build it
to Django static to serve a single application.

# IMPORTANT
THIS PROJECT IS STILL IN DEVELOPMENT!


# Pypi
* https://pypi.org/project/djangular-cli/1.2.1.dev2/

#### Version
![PyPI](https://img.shields.io/pypi/v/djangular-cli)


## TODO:
* Clean-up of code
* Add sister package support for DJANGULAR-SERVE
* Fix venv bugs
* Add more style

## Getting Started

Ensure you have the following prerequisites on your machine.

### Prerequisites

```
Node.js
npm
Angular-Cli
```

### Installing

It is best to install DJANGULAR-CLI globally.

```
pip install djangular-cli
or
pip3 install djangular-cli
```

To start a session, run:

```
djangular -g start
```

## Usage

Current commands in DJANGULAR-CLI.

```
Start client            : djangular -g start

Quick commands:
New Django project      : djangular - g django
New Angular project     : djangular -g angular
New Virtualenv          : djangular -env new
Activage Virtualenv     : djangular -env activate
Git Clone               : djangular -gc https://github.com/user/package
Build Angular to Django : djangular -srv .... [In development for sister package DJANGULAR-SERVE
```


## Deployment



## Built With
* [Python 3.8](https://python.org)

## Contributing
 
Open to contributions.

## Authors

* **Jonny Doyle** - *Initial work* - [LinkedIn](https://www.linkedin.com/in/jonnydoyle/)


## License

This project is licensed under the MIT License - see the [LICENSE](djangular_cli/docs/license/LICENSE) file for details

## Acknowledgments

* PyInquirer