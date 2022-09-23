#!/usr/bin/python3
'''
    Script sends a POST request to the passed URL
'''

if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    # Unpack input arguments
    try:
        url, email = argv[1:]
    # Catch error
    except ValueError as er:
        # msg (Error message)
        msg = 'Expect 2 arguments, (got {})'.format(len(argv[1:]))
        print(msg)
    else:
        # Execute if no error occur from unpack values

        # post data
        value = {'email': email}

        # Encode post data
        data = parse.urlencode(value)
        data = data.encode('ascii')

        # url + encode_data == url + query_string
        req = request.Request(url, data)

        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
