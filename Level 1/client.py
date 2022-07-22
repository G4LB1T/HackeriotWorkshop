import requests


def do_request():
    # INSERT SERVER ADDRESS HERE
    response = requests.get(?????)
    print(f'\n***************************\nRegular request result:\n{response.text}\n***************************\n')

if __name__ == '__main__':
    print('Trying normal python request:')
    do_request()
