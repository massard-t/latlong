#!/usr/bin/env python3
# coding: utf-8
'''
Simple module allowing you to get your latitude and longitude in multiple ways
'''
import sys
import requests
import re


URL = "http://wttr.in/~"
REGEX = r"\[([-+]?[0-9]*\.?[0-9]+,[-+]?[0-9]*\.?[0-9]+)\]"


def main():
    '''
    Main function, simply displays the result to stdout
    '''
    try:
        address = ' '.join(sys.argv[1:])
    except IndexError:
        print('No input found. Exiting...', file=sys.stderr)
        print('Usage: latlong ADDRESS')
        sys.exit(1)
    url = URL + address
    resp = requests.get(url)
    for line in resp.text.split('\n'):
        if line.startswith('Location'):
            coords = re.search(REGEX, line)
            break
    try:
        print(coords.group(1))
    except Exception as e:
        print('Unable to find address.', file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
