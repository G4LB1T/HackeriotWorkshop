import requests


def do_request():
    response = requests.get('http://localhost:8000')
    print(f'\n***************************\nRegular request result:\n{response.text}\n***************************\n')


if __name__ == '__main__':
    print('Trying normal python request:')
    do_request()
