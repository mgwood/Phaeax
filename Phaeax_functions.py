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


def find_function_paths(filename):
	
	f = open(filename, 'r')
        
        strings = re.findall(r'[def ]*[a-zA-Z_]+[\w.]*\(', f.read())

        out_strings = []
        
        for ii in range(len(strings)):
                match = re.search(r'^def[ ]*',strings[ii])
                
                if not match:
                        m = re.search(r'([\w.]*)(\.)([\w]*)',strings[ii])
                        if m:
                                out_strings.append('Call to: '+m.groups()[2])

                                m2 = re.search(r'([\w.]*)(\.)([\w]*)',m.groups()[0])
                                
                                while m2:
                                        out_strings.append('   From: '+m2.groups()[2])
                                        m2 = re.search(r'([\w.]*)(\.)([\w]*)',m2.groups()[0])
                                else:
                                        m2 = re.search(r'([\w]*)(\.)([\w]*)',m.groups()[0])
                                        if m2:
                                                out_strings.append('   From: '+m2.groups()[0]+'.py')
                                        else:
                                                out_strings.append('   From: '+m.groups()[0]+'.py')
                                                
                                continue
 
                        n = re.search(r'( )*([\w]*)',strings[ii])
 
                        if n:
                                out_strings.append('Call to: '+n.groups()[1])
                                out_strings.append('   From: '+filename)
                                continue
                        else:
                                print 'incorrect call format: '+strings[ii]                        
 
        return out_strings


def find_full_function_calls(filename):
	
	f = open(filename, 'r')
        
        strings = re.findall(r'[def ]*[a-zA-Z_]+[\w.]*\(', f.read())

        out_strings = []
        
        for ii in range(len(strings)):
                match = re.search(r'^def[ ]*',strings[ii])
                
                if not match:
                        m = re.search(r'([\w.]*)',strings[ii])
                        if m:
                                out_strings.append('Call to: '+m.groups()[0]+'.py')
                                continue
 
                        n = re.search(r'( )*([\w]*)',strings[ii])
 
                        if n:
                                out_strings.append('Call to: '+n.groups()[1])
                                out_strings.append('   From: '+filename)
                                continue
                        else:
                                print 'incorrect call format: '+strings[ii]                        
 
        return out_strings
