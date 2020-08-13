from pyfiglet import Figlet


def widget():
    f = Figlet(font='slant')
    print("DJANGULAR-CLI:  https://github.com/forafekt/djangular-cli  |  https://djangular.com \n")
    print("Please ensure the following are installed on your system: \n"
          "Nodejs:   'https://nodejs.org'\n"
          "npm:      'https://www.npmjs.com'\n"
          "Angular:  'https://www.npmjs.com/package/@angular/cli'\n")
    print(f.renderText('DJANGULAR.CLI'))
