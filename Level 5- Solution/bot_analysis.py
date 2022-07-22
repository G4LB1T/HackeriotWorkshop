def test_headers(req):
    headers = req.parse_headers()
    if 'python' in headers['User-Agent'] and 'Accept-Language' in headers:
        print('Python detected!')
        return False
    else:
        return True
