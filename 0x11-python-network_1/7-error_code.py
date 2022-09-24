#!/usr/bin/python3
'''
    Script demonstrates HTTP status code
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    # url
    url = argv[1]

    # Make HTTP GET request
    res = requests.get(url)

    # Retrieve request status code
    s_code = res.status_code

    if s_code >= 400:
        print('Error code: {}'.format(s_code))
    else:
        print(res.text)
