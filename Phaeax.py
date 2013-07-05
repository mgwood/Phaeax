'''
Phaeax

Michael Wood

June 19, 2013
'''

import Phaeax_functions

def main(filename):
    Phaeax_functions.print_full_file_analysis(filename)

    print Phaeax_functions.find_explicit_imports(filename)
    
main('Test_def_demo.py')
