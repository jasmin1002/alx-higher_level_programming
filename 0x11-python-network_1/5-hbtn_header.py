#!/usr/bin/python3
'''
    Script demonstrates HTTP GET request by 
    passed URL
'''

if __name__ == '__main__':
    import requests
    from sys import argv

    # url
    url = argv[1]

    # HTTP GET request
    res = requests.get(url)

    # Header's value
    print('{}'.format(res.headers.get('X-Request-Id')))
