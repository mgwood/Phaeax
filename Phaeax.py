'''
Phaeax

Michael Wood

June 19, 2013
'''

import Phaeax_functions

def main():
    print Phaeax_functions.find_imports('Test_def_demo.py')
    print Phaeax_functions.find_defs('Test_def_demo.py')
    out = Phaeax_functions.find_function_calls('Test_def_demo.py')

    for ele in out:
        print ele


main()
