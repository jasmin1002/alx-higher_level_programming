#!/usr/bin/python3
'''
    Script demostrates HTTPError class
    HTTPError is a subclass of URLError
'''

if __name__ == '__main__':
    from urllib import request
    from urllib.error import URLError
    from sys import argv

    # url
    url = argv[1]

    try:
        # Make HTTP GET request
        with request.urlopen(url) as response:
            # Get the byte string
            body = response.read()

            # Decode / parse byte string
            print(body.decode('utf-8'))

    except URLError as err:
        # Catch error and print response status code
        if hasattr(err, 'code'):
            msg = 'Error code: {}'.format(err.code)
            print(msg)
