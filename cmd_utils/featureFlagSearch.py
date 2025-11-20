#!/usr/bin/env python3
"""
Created on 19.11.2025

Makes a list of currently used feature flags in all subdirectories.
@author: piotr.strychaluk@j-labs.pl
"""

import mmap
import os
import re
import sys
from collections import defaultdict


EXCLUDED_DIRS = ['node_modules','coverage']


def return_first_subdir(file_path):
    relative_path = file_path[len(os.getcwd()):]
    return relative_path.split(os.sep)[1]


def check_if_directory_is_included(file_path):
    dirs = file_path.split(os.sep)
    for excluded_dir in EXCLUDED_DIRS:
        if excluded_dir in dirs:
            return False
    return True


def list_files_walk(start_path='.'):
    for root, directories, files in os.walk(start_path):
        for file in files:
            if re.findall(r'\.(js|ts|html|java|ftl)$', file, re.IGNORECASE):
                path = os.path.join(root, file)
                if os.stat(path).st_size > 0 and check_if_directory_is_included(path):
                    search_ff_in_file(path)


def search_ff_in_file(file_path):
    try:
        with open(file_path, 'rb', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as file:
            matches = re.finditer(br'luminator\?*.featureFlags\?*.isEnabled\([\n\r]*.*\'(.*)\'.*[\n\r]*.*\)', file, re.IGNORECASE|re.MULTILINE)
            for match in matches:
                ff_result[return_first_subdir(file_path)].add(match.group(1).decode())
    except IOError: print("Unable to open file: " + file_path, file=sys.stderr)
    except UnicodeDecodeError: print("Unable to decode file: " + file_path, file=sys.stderr)


print("============================")
print("Looking for feature flags...")
print("============================")
ff_result = defaultdict(set)
currentPath = os.getcwd()
list_files_walk(currentPath)
for key in ff_result:
    print('\nTop folder: ' + key)
    print('\t\tFlags used: ')
    for value in ff_result[key]:
        print("\t\t\t\t\t'" + value + "'")
