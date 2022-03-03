#!/usr/bin/python3
"""The main command line for the backend of the airbnb project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Cmd SubClass."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, arg):
        """Quit command to exit the program."""
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
