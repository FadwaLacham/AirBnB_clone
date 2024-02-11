#!/usr/bin/env python3
"""entry to the program
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """cmd class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_EOF(self, line):
        """Command to end the program"""
        return True

    def do_quit(self, line):
        """Command to end the program"""
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        classes = {"BaseModel": BaseModel, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review, "User": User}
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        classes = {"BaseModel": BaseModel, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review, "User": User}
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
        else:
            print(all_objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        classes = {"BaseModel": BaseModel, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review, "User": User}
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of instances"""
        args = line.split()
        all_objects = storage.all()
        obj_list = []
        if not args:
            for obj_key, obj_val in all_objects.items():
                obj_list.append(str(obj_val))
        else:
            class_name = args[0]
            classes = {"BaseModel": BaseModel, "State": State,
                       "City": City, "Amenity": Amenity, "Place": Place,
                       "Review": Review, "User": User}
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            for obj_key, obj_val in all_objects.items():
                if obj_val.__class__.__name__ == class_name:
                    obj_list.append(str(obj_val))
        print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        classes = {"BaseModel": BaseModel, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review, "User": User}
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        obj_instance = all_objects[key]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj_instance, attribute_name, attribute_value)
        storage.save()

    def do_count(self, line):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()

        commands = line.split()

        if line:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        arg_list = arg.split('.')

        if len(arg_list) == 2:
            cls_nm = arg_list[0]  # incoming class name
            command = arg_list[1].split('(')
            cmd_met = command[0]  # incoming command method
            e_arg = command[1].split(')')[0]  # extra arguments

            method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
            }

            if cmd_met in method_dict.keys():
                try:
                    call = method_dict[cmd_met]
                    return call("{} {}".format(cls_nm, e_arg))
                except Exception:
                    pass

        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
