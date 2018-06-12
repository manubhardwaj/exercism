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
    i = i.split('/')
    subtree = s
    for dirname in i:
        if dirname not in subtree:
            subtree[dirname] = {}
        subtree = subtree[dirname]

#print(yaml.dump(s))
