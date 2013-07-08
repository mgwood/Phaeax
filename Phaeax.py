'''
Phaeax

Michael Wood

June 19, 2013
'''

'''Current status:

1. Single file version fully working as a demo
2. Still need to re-impliment the print-out and error checking
3. Next up is allowing for multiple input files where the outputs are stored
   as an array of dictionaries (or a dict where key = filename, val = dict)
4. After that, we will need functions to find connections between each file
'''


import Phaeax_functions

def main(filename):
    #Phaeax_functions.print_full_file_analysis(filename)

    #print Phaeax_functions.find_all_imports(filename)

    print Phaeax_functions.build_namespace(filename)
    #print Phaeax_functions.find_full_function_calls(filename)
    
main('Test_def_demo.py')
