#!/usr/local/bin/python3

# Check if using local environment
from os import getenv
import os.path
if getenv('ENVIRONMENT') == 'local':
    import sys
    from sys import path

    path.append('../../includes')
    from __init__ import data

from test_parent import BaseTest
import util
import unittest


class TCP4_767(BaseTest):
    ''' Test to verify import a collections'''

    def test_import_collection(self):
        file_name = 'id2.png'
        # print(os.path.abspath(file_name), file=sys.stderr)
        self.log.append(os.path.abspath(file_name))
        cwd = os.getcwd()
        self.log.append(cwd)



if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_767, data, __main__)
