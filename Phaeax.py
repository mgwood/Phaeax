'''
Phaeax

Michael Wood

June 19, 2013
'''

import Phaeax_functions

def main(filename):
    Phaeax_functions.print_full_file_analysis(filename)

    print Phaeax_functions.find_all_imports(filename)

    print Phaeax_functions.build_namespace(filename)
    print Phaeax_functions.find_full_function_calls(filename)
    
main('Test_def_demo.py')
