#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""console module.
- Class HBNBCommand - A class inheriting from cmd.Cmd acting as a shell
                      for testing the storage engine of the HBnB project.
- Instance Attributes (public):
      - prompt: The prompt to be shown.
- Methods (public):
      - do_quit: Exits the shell.
      - do_EOF: Exits the shell.
      - do_create: Creates a new instance of an object and prints its id.
      - do_show: Shows the string representation of an object given its class
                 name and id.
"""
import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The shell for the HBnB project.
    Attributes:
        prompt (str): The shell prompt.
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Amenity", "City",
                  "Place", "Review", "State"]

    def do_quit(self, arg):
        """\
        Quit command. Exits hbnb shell.\
        """
        return True

    def do_EOF(self, arg):
        """\
        EOF command. Exits hbnb shell.\
        """
        return True

    def empty_line(self):
        """\
        Empty line function. Does nothing.\
        """
        return

    def do_create(self, arg):
        """\
        Creates a new instance of type TYPE, saves it as JSON and prints
        its id.
            Usage: create TYPE
            Example: create BaseModel\
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        obj = eval(arg + "()")
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """\
        Prints a string representation of an instance type TYPE with id ID.
            Usage: show TYPE ID
            Example: show BaseModel 1234-1234-1234\
        """
        arg_list = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        for key, value in storage.all().items():
            if key.split(".")[1] == arg_list[1]:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """\
        Deletes an instance type TYPE with id ID and saves the changes
        in a JSON file.
            Usage: destroy TYPE ID
            Example: destroy BaseModel 1234-1234-1234\
        """
        arg_list = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, arg):
        """\
        Prints a string representation of type TYPE or all types.
            Usage: all [TYPE]
            Examples: all
                      all BaseModel
        """
        arg_list = arg.split(" ")
        if arg:
            if arg_list[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
            obj_list = []
            for key, val in storage.all().items():
                if key.split(".")[0] == arg_list[0]:
                    obj_list.append(str(val))
            print(obj_list)
            return
        obj_list = [str(val) for val in storage.all().values()]
        print(obj_list)

    def do_update(self, arg):
        """\
        Updates an instance of type TYPE and id ID with ATTRIBUTE_NAME
        and ATTRIBUTE_VALUE and saves it to a JSON file.
            Usage: update TYPE ID ATTRIBUTE_NAME ATTRIBUTE_VALUE
            Example: update BaseModel 1234-1234-1234 email "hbnb@hlbrtn.com"\
        """
        arg_list = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, arg_list[2], arg_list[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
