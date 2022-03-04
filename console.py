#!/usr/bin/python3
"""The main command line for the backend of the airbnb project."""
import cmd
from models.base_model import BaseModel, storage

class HBNBCommand(cmd.Cmd):
    """Cmd SubClass."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        exit()

    def do_EOF(self, arg):
        """
        Quit command to exit the program.
        """
        exit()

    def do_create(self, arg):
        """
        Create a new instance of Baseclass and save it.

        Usage: create [Class Name]
        """

        if arg == "":
            print("** class name missing **")

        elif class_exist(arg):
            print("** class doesn't exist **")

        else:
            new_instance = BaseModel() 
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show representation of object by id.

        Usage: show [class name] [id]
        """
        obj = arg.split(' ')

        if arg == "":
            print("** class name missing **")
        else:
            if class_exist(obj[0]):
                print("** class doesn't exist **")
            elif len(obj) == 1:
                print("** instance id missing **")
            else:
                objs = storage.all()
                obj = obj[0]+'.'+obj[1]
                if obj in objs: 
                    print(objs[obj])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes instance of class by idself.
        Usage: destro [class] [id]
        """
        obj = arg.split(' ')

        if arg == "":
            print("** class name missing **")
        else:
            if class_exist(obj[0]):
                print("** class doesn't exist **")
            elif len(obj) == 1:
                print("** instance id missing **")
            else:
                objs = storage.all()
                obj = obj[0]+'.'+obj[1]
                if obj in objs: 
                    del objs[obj]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Show all objects.

        Usage: all [[class]]
        """
        objs = storage.all()

        if arg == "":
            obj_str = []
            for obj in objs:
                obj_str.append(str(objs[obj]))
            print(obj_str)

        else:
            obj_str = []
            if class_exist(arg):
                print("** class doesn't exist **")
            else:
                for obj in objs:
                    if objs[obj].to_dict()['__class__'] == arg:
                        obj_str.append(str(objs[obj]))
                print(obj_str)

    def do_update(self, arg):
        """
        Upadate the object with attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split(' ')

        if arg == "":
            print("** class name missing **")

        elif class_exist(args[0]):
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            objs = storage.all()
            obj = args[0] + '.' + args[1]
            if obj in objs: 
                if len(args) == 2:
                    print("** attribute name missing **")
                if len(args) == 3:
                    print("** value missing **")
                else:
                    args[3] = args[3].strip("\"'")
                    if hasattr(objs[obj], args[2]):
                        if type(getattr(objs[obj], args[2])) is str:
                            args[3] = str(args[3])
                        elif type(getattr(objs[obj], args[2])) is int: 
                            args[3] = int(args[3])
                        elif type(getattr(objs[obj], args[2])) is float: 
                            args[3] = float(args[3])

                    setattr(objs[obj], args[2], args[3])
            else:
                print("** no instance found **")


def class_exist(_class):
    classes = ["BaseModel"]
    return _class not in classes


if __name__ == '__main__':
    HBNBCommand().cmdloop()
