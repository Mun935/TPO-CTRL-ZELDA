import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface import print_console
from interface import read_console
from interface import menu_handlers

def main():
    while True:
        print_console.print_login()
        option = read_console.get_option(1, 3)

        match option:
            case 1:
                menu_handlers.handle_log_option()
            case 2:
                menu_handlers.handle_new_user_menu()
            case 3:
                break

    print("Gracias por utilizar nuestro sistema. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()
