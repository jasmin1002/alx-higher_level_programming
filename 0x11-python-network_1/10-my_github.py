#!/usr/bin/python3
'''
    Script demonstrates GitHub API
'''

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    # url
    url = 'https://api.github.com/user'

    # Unpack passed arguments
    # username: account's username
    # token: account's Personal Access Token (PAT)
    try:
        username, token = argv[1:]

    except ValueError as err:
        # Catch error and
        # describe no. of arguments required
        msg = 'Expect only username and password as arguments'
        print(msg)

    # Provided authentication credentials
    credential = HTTPBasicAuth(username, token)

    # Make HTTPS GET request
    res = requests.get(url, auth=credential)

    if res.status_code == 200:
        dict_data = res.json()
        print(dict_data['id'])
    else:
        print('None')
