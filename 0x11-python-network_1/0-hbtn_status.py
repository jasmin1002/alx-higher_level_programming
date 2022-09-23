#!/usr/bin/python3
'''Script fetches data from https://alx-intranet.hbtn.io/status'''

if __name__ == '__main__':
    from urllib import request

    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        body = response.read()
        msg = '\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'\
            .format(type(body), body, body.decode("utf-8"))

        print('Body response:')
        print(msg)
