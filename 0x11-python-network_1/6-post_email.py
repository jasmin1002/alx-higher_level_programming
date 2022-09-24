#!/usr/bin/python3
'''
    Script demonstrates HTTP POST request
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    # Unpack input arguments
    try:
        url, email = argv[1:]

    except ValueError as err:
        # Capture error raise by list unpack
        # Error message
        msg = 'Expect 2 arguments, (got {})'.format(argv[1:])
        print(msg)

    else:
        # Make HTTP POST request on successful value unpack
        res = requests.post(url, data={'email': email})
        print(res.text)
