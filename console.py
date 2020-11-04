#!/usr/bin/python3
"""
This module defines a HBNBCommand class
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Defines a HBNBCommand
    """
    prompt = '(hbnb) '
    __Base_models = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__Base_models

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
        elif args[0] not in self.all().keys():
            print("** class doesn't exist **")
        else:
            new_instance = self.all()[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        arg_split = arg.split()
        if len(arg_split) == 0:
            print("** class name missing **")
        elif len(arg_split) == 1:
            if arg_split[0] not in self.all().keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg_split) > 1:
            if arg_split[0] not in self.all().keys():
                print("** class doesn't exist **")
            else:
                base_object = storage.all()
                key_word = arg_split[0] + '.' + arg_split[1]
                if key_word not in base_object.keys():
                    print("** no instance found **")
                else:
                    print(base_object[key_word])

    def do_all(self, arg):
        """show all instances of a class"""
        arg_split = arg.split()
        base_object = storage.all()
        list = []
        if len(arg_split) == 0:
            for key_word in base_object.keys():
                list.append(base_object[key_word].__str__())
        else:
            if arg_split[0] not in self.all().keys():
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
        
        store = storage.all()
        for i in range(len(arg)):
            if arg[i] == "{" and arg[-1] == "}":
                args = arg[:i].split()
                if args[0] not in self.all().keys():
                    print("** class doesn't exist **")
                elif str(args[0]) + "." + str(args[1]) not in storage.all().keys():
                    print("** no instance found **")
                else:
                    my_dict = eval(arg[i:])
                    for key, value in my_dict.items():
                        setattr(store[(args[0]) + "." + (args[1])], key, value)
                        storage.save()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.all().keys():
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
        elif args[0] not in self.all().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + '.' + args[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()

    def default(self, arg):
        """advanced task, default"""
        args = arg.split(".")
        if len(args) == 2:
            if args[0] in self.all().keys():
                split_methods = args[1].split("(")
                if len(split_methods) >= 2:
                    store = storage.all()
                    try:
                        if split_methods[1][-1] == ")":
                            split_methods[1] = split_methods[1][:-1]
                        else:
                            return
                    except Exception:
                        return
                    if split_methods[0] == "all":
                        self.do_all(args[0])
                    if split_methods[0] == "count":
                        count = 0
                        for key, value in store.items():
                            keys = key.split(".")
                            if keys[0] == args[0]:
                                count += 1
                        print(count)
                    if split_methods[0] == "show":
                        self.do_show(args[0] + " " + split_methods[1])
                    if split_methods[0] == "destroy":
                        self.do_destroy(args[0] + " " + split_methods[1])
                    if split_methods[0] == "update":
                        n_list = []
                        try:
                            for i in range(len(split_methods[1])):
                                if (split_methods[1][0] == "\"" and split_methods[1][i] == "\""):
                                    n_list.append(split_methods[1][1:i])
                                if (split_methods[1][i] == "{" and split_methods[1][-1] == "}"):
                                    n_list.append(split_methods[1][i:-1] + "}")
                                    n_list.remove('')
                                    self.do_update(args[0] + " " + n_list[0] + " " + n_list[1])
                                    return
                        except:
                            return
                        split_inside = split_methods[1].replace(" ", "")
                        split_inside2 = split_inside.split(",")
                        n_list = []
                        if (len(split_inside2) <= 3):
                            try:
                                for i in split_inside2:
                                    if split_inside2[2] == i:
                                        if i[-1] == "\"" and i[0] == "\"":
                                            n_list.append(i[1:-1])
                                            continue
                                        n_list.append(split_inside2[2])
                                    elif i[-1] == "\"" and i[0] == "\"":
                                        n_list.append(i[1:-1])
                                    else:
                                        n_list.append(" ")
                                for v in range(len(n_list), 3):
                                    n_list.append("")
                                self.do_update(args[0] + " " + n_list[0] +
                                               " " + n_list[1] + " " +
                                               n_list[2])
                            except Exception:
                                return
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
