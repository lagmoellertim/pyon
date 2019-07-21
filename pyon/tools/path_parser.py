import json


def parse(path):
    """
    Validate and Optimise a path string
    Example: "/pyon/./../test/" -> "/test/"
    Example: "//pyon" -> Invalid
    :param path:
    :return:
    """

    if not path.startswith("/") or not path.endswith("/") or "//" in path:
        raise ValueError("The path '{}' is invalid".format(path))

    path_segments = path.split("/")[1:-1]
    converted_path_segments = convert_type(path_segments)

    parsed_path_segments = []
    for path_segment in converted_path_segments:
        if path_segment in ["..", "."]:
            if path_segment == "..":
                if parsed_path_segments:
                    parsed_path_segments.pop(-1)
        else:
            parsed_path_segments.append(path_segment)

    return parsed_path_segments


def convert_type(base_list):
    """
    Convert a list of strings into their native python types
    Example: ["pyon", "1", "1.5"] -> ["pyon", 1, 1.5]
    :param base_list: List of strings
    :return: Converted list of native types
    """

    converted_list = []

    for item in base_list:
        try:
            converted_list.append(json.loads(item))
        except ValueError:
            converted_list.append(item)

    return converted_list


def join(*path_segments):
    """
    Join together multiple paths
    Example: "/", "pyon", "123", "../" -> "/pyon/123/../"
    :param path_segments:
    :return:
    """

    joined_path = ""
    for path_segment in path_segments:
        if path_segment.startswith("/"):
            joined_path = path_segment
        else:
            joined_path += path_segment
        if not path_segment.endswith("/"):
            if not(joined_path.endswith("/") and path_segment == ""):
                joined_path += "/"

    return joined_path


def insert_values(path, instance):
    """
    Insert values from object into the path string
    Example: "/{test}/" (self.test = "pyon") -> "/pyon/"
    :param path: Path string where the values should be inserted
    :param instance: Instance (mostly 'self') which includes the values
    :return:
    """

    return path.format(**vars(instance))
