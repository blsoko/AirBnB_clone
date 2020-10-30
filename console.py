#!/usr/bin/python3
"""
This module defines a HBNBCommand class
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Defines a HBNBCOmmand
    """
    prompt = '(hbtn) '

    def emptyline(self):
        """overwrites the emptyline method"""
        pass

    def do_quit(self, arg):
        """Stop the console"""
        return True

    def do_EOF(self, arg):
        """Stop if: end of file"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        basemodel = ['BaseModel']
        arg_split = arg.split()
        if len(arg_split) == 0:
            print("** class name missing **")
        elif len(arg_split) == 1:
            if arg_split[0] not in basemodel:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg_split) > 1:
            if arg_split[0] not in basemodel:
                print("** class doesn't exist **")
            else:
                base_object = storage.all()
                key_word = arg_split[0] + '.' + arg_split[1]
                if key_word not in base_object.keys():
                    print("** no instance found **")
                else:
                    print(base_object[key_word])

    def do_all(self, arg):
        """show all BaseModel"""
        basemodel = ['BaseModel']
        arg_split = arg.split()
        base_object = storage.all()
        list = []
        if len(arg_split) == 0:
            for key_word in base_object.keys():
                list.append(base_object[key_word].__str__())
        else:
            if arg_split[0] not in basemodel:
                print("** class doesn't exist **")
                return
            for key in base_object.keys():
                obj = key.split('.')[0]
                if arg_split[0] == obj:
                    list.append(base_object[key].__str__())
        print(list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + '.' + args[1] not in storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            # Quitar las comillas dobles del args[3]
            if args[3][0] == "\"":
                args[3] = args[3][1:-1]
            setattr(storage.all()[args[0] + '.' + args[1]], args[2], args[3])
            storage.all()[args[0] + '.' + args[1]].save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + '.' + args[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
