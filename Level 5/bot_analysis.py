def test_headers(req):
    headers = req.parse_headers()
    if 'python' in headers['User-Agent'] and ?????????:
        print('Python detected!')
        return False
    else:
        return True
