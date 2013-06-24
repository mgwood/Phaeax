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

        function_calls_dict = {}
        
        for ii in range(len(strings)):
                match = re.search(r'^def[ ]*',strings[ii])
                
                if not match:
                        m = re.search(r'( )*([\w\.]*)',strings[ii])
                        if m:
                                function_calls_dict[m.groups()[1]] = function_calls_dict.get(m.groups()[1],0) + 1

 
        return function_calls_dict


def find_required_imports(filename):

        call_dict = find_full_function_calls(filename)

        unused_imports = find_imports(filename)
        used_imports = []
        needed_imports = []
        for c in call_dict.keys():
                m = re.search(r'( )*([\w]*)(\.)([\w\.]*)',c)
                if m:
                        if m.groups()[1] in unused_imports:
                                used_imports.append(m.groups()[1])
                                unused_imports.remove(m.groups()[1])

                        else:
                                if m.groups()[1] not in used_imports:
                                        if m.groups()[1] not in needed_imports:                                        
                                                needed_imports.append(m.groups()[1])
                                                
        
        return [used_imports,unused_imports,needed_imports]

def find_required_defs(filename):

        call_dict = find_full_function_calls(filename)
        
        unused_defs = find_defs(filename)
        used_defs = []
        needed_defs = []
        
        for c in call_dict.keys():
                m = re.search(r'( )*([\w]*)(\.)([\w\.]*)',c)
                if not m:
                        if c in unused_defs:
                                used_defs.append(c)
                                unused_defs.remove(c)
                        else:
                                if c not in used_defs:
                                        if c not in needed_defs:                                        
                                                needed_defs.append(c)
                                                
        
        return [used_defs,unused_defs,needed_defs]

def print_file_analysis(filename, imports, defs, paths, call_dict,import_analysis,def_analysis):

        print 'Analysis of '+filename+':'
        print ' '
        print ' '

        print 'Import statements:'
        for im in imports:
                print im
        print ' '
        print 'Import analysis:'
        im_flag = True
        
        if not import_analysis[1]==[]:
                print 'Unsued imports:'
                im_flag = False
                for im in import_analysis[1]:
                        print im
                        
        if not import_analysis[2]==[]:
                print 'Needed imports not included:'
                im_flag = False
                for im in import_analysis[2]:
                        print im

        if im_flag:
                print 'No import errors'
        print ' '

        print 'Defined functions:'
        for d in defs:
                print d
        print ' '
        print 'Function analysis:'
        def_flag = True
        
        if not def_analysis[1]==[]:
                print 'Unsued functions:'
                def_flag = False
                for im in def_analysis[1]:
                        print im
                        
        if not def_analysis[2]==[]:
                print 'Needed defs not included:'
                def_flag = False
                for im in def_analysis[2]:
                        print im

        if def_flag:
                print 'No def errors'
        print ' '

        print 'List of called fuctions: '
        key_order = sorted(call_dict,key=call_dict.get)
        key_order.reverse()

        for k in key_order:
                print str(call_dict[k])+' : '+str(k)
        print ' '
        

def print_full_file_analysis(filename):

        print_file_analysis(filename, find_imports(filename), find_defs(filename),\
                            find_function_paths(filename), find_full_function_calls(filename)\
                            ,find_required_imports(filename),find_required_defs(filename))
        
