#!/usr/bin/env python

import sys

keywords = ['game','players','draft','team','amp','nfl','cricket','nba','soccer','baseball']

def foundKeyword(line):
    for keyword in keywords:
        if keyword in line:
            return keyword
    return "_undefined_"

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    found = foundKeyword(line)
    if found != "_undefined_":
        words = line.split(' ')
        for word in words:
            if word != found:
                print ("{0}|{1}\t{2}".format(found, word, 1))