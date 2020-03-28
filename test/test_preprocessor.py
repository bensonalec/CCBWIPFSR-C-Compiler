import sys
import os
sys.path.append('../src/frontend')

import unittest
from preprocessor import run

path_to_C_files = "./programs/"
path_to_output_files = "./expected_output/preprocessor/"

class PreProcessorTests(unittest.TestCase):

    # Add program into list if for some reason, we shouldn't test it.
    skip_programs = []

    maxDiff = None

    def test_preProcessor(self):
        print(' ')

        for c_filename in sorted(os.listdir(path_to_C_files)):

            if c_filename.endswith('.c') and c_filename not in self.skip_programs:

                status = "FAIL" #Will change if test passes

                fi = open(path_to_C_files + c_filename)
                text_input = fi.read()
                fi.close()

                # Naming scheme for expected output is same as C-file, but no extension
                expected_filename = os.path.splitext(c_filename)[0]
                fi = open(path_to_output_files + expected_filename)
                expected = fi.read()
                fi.close()

                with self.subTest():
                    self.assertEqual(run(text_input, path_to_C_files + c_filename), expected)
                    status = "ok"

                print(f"{'PreProcessor test for '+c_filename:65}", end="")
                if status == "ok":
                    print(Colors.green, f"{status}", Colors.reset)
                else:
                    print(Colors.red, f"{status}", Colors.reset)

            elif c_filename.endswith('.c'):
                print(f"{'PreProcessor test for '+c_filename:65}", end="")
                print(Colors.blue, "skipped", Colors.reset)

class Colors:
        red='\033[31m'
        green='\033[32m'
        blue='\033[34m'
        reset='\033[00m'

if __name__ == '__main__':
	unittest.main()

