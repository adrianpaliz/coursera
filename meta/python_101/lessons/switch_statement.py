http_status = 502


if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not found')
elif http_status == 500 or http_status == 501:
    print('Server Error')
else:
    print('Unknown')
