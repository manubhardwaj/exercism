#!/usr/bin/env python3

#import yaml

inputs = [
        '/home/manu/1/2',
        '/home/manu/3',
        '/drugs/A',
        '/drugs/B/C',
        '/home/manu/3/4'
]

s = {}

for i in inputs:
    # Tokenize the inputs into a list, e.g. "/drugs/A" becomes ['drugs','A']
    i = i.split('/')
    subtree = s

    # Go from left to right in the list, creating a dict in each case
    for dirname in i:

        # Create the dict of the current element
        if dirname not in subtree:
            subtree[dirname] = {}

        # Now go deeper into the list, to recursively construct subdicts
        subtree = subtree[dirname]

# Pretty printing for testing
#print(yaml.dump(s))
