#!/usr/bin/python3
'''
    Script uses requests library
'''

if __name__ == '__main__':
    import requests

    # url
    url = 'https://alx-intranet.hbtn.io/status'

    # HTTP GET request
    res = requests.get(url)

    # Retrieve the decode or parse text string
    content = res.text

    # Print format
    output = 'Body response:\n\t- type: {}\n\
        - content: {}'.format(type(content), content)
    print(output)
