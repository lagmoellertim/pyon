import unittest
from pyon.tools import path_parser
from pyon.tests.tools.print_message import print_start


class PathParserTest(unittest.TestCase):
    def test_parse_on_valid_paths(self):
        print_start("parse_on_valid_paths")
        test_set = {
            "/": [],
            "/test/": ["test"],
            "/test/123/*/": ["test", 123, "*"],
            "/test/123/././././": ["test", 123],
            "/test/../abc/1.4/./5/../5/*/": ["abc", 1.4, 5, "*"]
        }

        for path, parsed_path in test_set.items():
            print("Path: '{}'".format(path))
            output = path_parser.parse(path)
            self.assertEqual(parsed_path, output)

    def test_parse_on_invalid_paths(self):
        print_start("parse_on_invalid_paths")
        test_set = {
            "/*": ValueError,
            "/test/123//abc/": ValueError,
            "": ValueError,
            "test/": ValueError
        }

        for path, exception in test_set.items():
            print("Path: '{}'".format(path))
            self.assertRaises(exception, path_parser.parse, path)

    def test_convert_type(self):
        print_start("convert_type")
        test_set = [
            [["1", "2.1", "('Test')"], [1, 2.1, "('Test')"]],
            [["[1,2,3]", "5"], [[1, 2, 3], 5]]
        ]

        for test in test_set:
            string_list, converted_list = test
            print("List: '{}'".format(string_list))
            output = path_parser.convert_type(string_list)
            self.assertEqual(converted_list, output)

    def test_join_on_valid_paths(self):
        print_start("join_on_valid_paths")
        test_set = [
            [["/test/", "123", "*"], "/test/123/*/"],
            [["/test", "../", "./", "*", "../"], "/test/.././*/../"],
            [["/test", "/test2"], "/test2/"]
        ]

        for test in test_set:
            path_list, joined_path = test
            print("List: '{}'".format(path_list))
            output = path_parser.join(*path_list)
            self.assertEqual(joined_path, output)

    def test_insert_value(self):
        print_start("insert_value")

        class TestInstance:
            def __init__(self):
                self.val1 = 1
                self.val2 = 2
                self.val3 = 3
                self._val4 = 4

        path1 = "/{val1}/{val2}-{val3}.{_val4}/"
        formatted_path1 = "/1/2-3.4/"
        path2 = "/{val1}/{val2}-{val3}.{_val5}/"

        instance = TestInstance()

        print(path1)
        output = path_parser.insert_values(path1, instance)
        self.assertEqual(formatted_path1, output)

        print(path2)
        self.assertRaises(KeyError, path_parser.insert_values, path2, instance)
