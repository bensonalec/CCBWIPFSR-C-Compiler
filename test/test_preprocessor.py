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
        print()

        for c_filename in os.listdir(path_to_C_files):
            
            if c_filename.endswith('.c') and c_filename not in self.skip_programs:

                print (f"Testing: {c_filename}")

                fi = open(path_to_C_files + c_filename)
                text_input = fi.read()
                fi.close()

                # Naming scheme for expected output is same as C-file, but no extension
                expected_filename = os.path.splitext(c_filename)[0]
                fi = open(path_to_output_files + expected_filename)
                expected = fi.read()
                fi.close()

                self.assertEqual(run(text_input), expected)
                print(f"PreProcessor test passed with: {c_filename}")

if __name__ == '__main__':
	unittest.main()

