#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }


class FileStorage:
    """The file storage engine class, that is;
    A class that serialize and deserialize instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary of objects."""
        if not cls:
            return self.__objects
        elif isinstance(cls, str):
            return {key: value for key, value in self.__objects.items()
                    if value.__class__.__name__ == cls}
        else:
            return {key: value for key, value in self.__objects.items()
                    if value.__class__ == cls}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
            with open(type(self).__file_path, "w", encoding='utf-8') as file:
                json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if os.path.exists(type(self).__file_path):
            try:
                with open(
                        type(self).__file_path,
                        "r", encoding="utf-8") as file:
                    obj_dict_list = json.load(file)
                    for obj_dict in obj_dict_list:
                        obj_class = class_dict[obj_dict["__class__"]]
                        obj_instance = obj_class(**obj_dict)
                        key = "{}.{}".format(
                            obj_dict["__class__"],
                            obj_dict["id"]
                        )
                        self.__objects[key] = obj_instance
            except Exception as e:
                pass

    def delete(self, obj=None):
        """An instance that  deletes obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """deserializes JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """ method to retrieve one object """
        if cls is not None:
            match = list(
                    filter(
                        lambda x: type(x) is cls and x.id == id,
                        self.__objects.values()
                        )
                    )
            if match:
                return match[0]
        return None

    def count(self, cls=None):
        """ Counts the number of objects in the storage """
        return len(self.all(cls))
