'''
Phaeax helper functions

Michael Wood
June 19, 2013
'''

import re

def find_imports(filename):

        f = open(filename, 'r')
        
        strings = re.findall(r'import [a-zA-Z_]+[\w]*', f.read())

        for ii in range(len(strings)):
                strings[ii] = re.sub(r'^import[ ]*', '', strings[ii])

        return strings


def find_defs(filename):
	
	f = open(filename, 'r')
        
        strings = re.findall(r'def [a-zA-Z_]+[\w]*', f.read())

        for ii in range(len(strings)):
                strings[ii] = re.sub(r'^def[ ]*', '', strings[ii])

        return strings


def find_function_calls(filename):
	
	f = open(filename, 'r')
        
        strings = re.findall(r'[def ]*[a-zA-Z_]+[\w.]*\(', f.read())

        for ii in range(len(strings)):
                match = re.search(r'^def[ ]*',strings[ii])

                if not match:
                        m = re.search(r'([\w]*).+([\w]*)',strings[ii])
                        


def num_groups(regex):
    return re.compile(regex).groups








        
