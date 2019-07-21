from pyon.tools import path_parser, json_generator
import json


class PyonObject:
    def __init__(self, path=""):
        """
        Initialises the Pyon Object
        :param path: Set the path for the JSON generator
        """

        self.__pyon_object_path = path

    def generate_json(self, file_object=None, allow_overwrite=False):
        """
        Generates the JSON object
        :param file_object: Specify a file the JSON object get written to, only returns the data when not specified
        :param allow_overwrite: Whether objects that are written later can overwrite those that were written earlier
        :return: The JSON object
        """

        object_path_list = self.__get_object_path_list(is_base_object=True)
        json_object = json_generator.generate_json(object_path_list, allow_overwrite=allow_overwrite)

        if file_object is not None:
            with file_object as f:
                f.write(json.dumps(json_object))

        return json_object

    def __get_object_path_list(self, parent_path="/", is_base_object=False):
        """
        Get the object_path_list which is used by the JSON generator
        :param parent_path: The path of the parent PyonObject
        :param is_base_object: Whether this is the PyonObject the generate_json function got called on
        :return: The object_path_list
        """

        if "_PyonObject__pyon_object_path" not in vars(self).keys():
            self.__pyon_object_path = ""

        joined_path = path_parser.join(parent_path, self.__pyon_object_path)
        path = path_parser.insert_values(joined_path, self)

        object_path_list = []
        instance_vars = {}

        for key, value in vars(self).items():
            path_extension = key if (path == "/" and is_base_object) else ""

            if not key.startswith("_"):
                if isinstance(value, PyonObject):
                    object_path_list.append(*value.__get_object_path_list(
                        parent_path=path_parser.join(path, path_extension)
                    ))

                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, PyonObject):
                            object_path_list.append(*item.__get_object_path_list(
                                parent_path=path_parser.join(path,
                                                             path_extension,
                                                             "*" if (path == "/" and is_base_object) else ""
                                                             )
                            ))

                else:
                    instance_vars[key] = value

        object_path_list.insert(0, (instance_vars, path))

        return object_path_list
