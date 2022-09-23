#!/usr/bin/python3
'''
    Script displays content of Response header
'''
if __name__ == '__main__':
    from urllib import request
    from sys import argv

    url = argv[1]

    with request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
