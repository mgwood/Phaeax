'''
Phaeax

Michael Wood

June 19, 2013
'''

import Phaeax_functions

def main():
    imports = Phaeax_functions.find_imports('Test_def_demo.py')
    defs =  Phaeax_functions.find_defs('Test_def_demo.py')
    paths = Phaeax_functions.find_function_paths('Test_def_demo.py')
    call_dict = Phaeax_functions.find_full_function_calls('Test_def_demo.py')


    Phaeax_functions.print_file_analysis('Test_def_demo.py', imports, defs, paths, call_dict)
    
main()
