import unittest
import unittest.mock as mock

import pyon
from pyon.tests.tools.print_message import print_start


class PyonObjectTest(unittest.TestCase):
    def test_dump_on_valid_inputs(self):
        print_start("dump_on_valid_inputs")
        test_set = {
            (None, "json", False): {'test': {}},
            (None, "xml", False): b'<?xml version="1.0" encoding="UTF-8" ?><root><test></test></root>',
            (None, "yaml", False): 'test: {}\n',
        }
        p = pyon.PyonObject(path="/test/")
        for dump_input, expected in test_set.items():
            file_handler, output_format, overwrite = dump_input
            output = p.dump(output_format=output_format)
            self.assertEqual(expected, output)

    def test_dump_on_invalid_inputs(self):
        print_start("dump_on_invalid_inputs")
        test_set = {
            (None, "", False): ValueError,
        }
        p = pyon.PyonObject(path="/test/")
        for dump_input, expected in test_set.items():
            file_handler, output_format, overwrite = dump_input
            with self.assertRaises(expected):
                p.dump(output_format=output_format)
