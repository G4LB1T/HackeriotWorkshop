import requests


def do_request():
    response = requests.get('http://localhost:8000')
    print(f'\n***************************\nRegular request result:\n{response.text}\n***************************\n')


def do_stealth_request():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get('http://localhost:8000', headers=headers)
    print(f'\n***************************\nStealth request result:\n{response.text}\n***************************\n')


if __name__ == '__main__':
    print('Trying normal python request:')
    do_request()
    print('Trying stealthy python request:')
    do_stealth_request()
