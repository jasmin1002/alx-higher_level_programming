#!/usr/bin/python3
'''
    Script demonstrates json and requests usage
'''

if __name__ == '__main__':
    from sys import argv
    from requests import codes
    import requests

    # url
    url = 'http://0.0.0.0:5000/search_user'

    # query value
    q = ''

    try:
        q = argv[1]
    except IndexError:
        print('No result')
    else:
        res = requests.post(url, data={'q': q})
        data = res.json()
        if len(data) == 0:
            print('No result')
        elif res.status_code != codes.ok:
            print('Not a valid JSON')
        else:
            print('[{}] {}'.format(data['id'], data['name']))
