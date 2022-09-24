#!/usr/bin/python3
'''
    Script demonstrates json and requests usage
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    # url
    url = 'http://0.0.0.0:5000/search_user'

    # query value
    q = ''

    if len(argv) < 2:
        q = ''
    else:
        q = argv[1]

    try:
        res = requests.post(url, data={'q': q})
        data = res.json()
        if len(data) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(data['id'], data['name']))
    except requests.exceptions.HTTPError:
        print('Not a valid JSON')
