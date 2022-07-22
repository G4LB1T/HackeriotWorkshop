def test_headers(req):
    headers = req.parse_headers()
    # ADD MISSING PART HERE
    if ????? in headers['User-Agent']:
        print('Python detected!')
        return False
    else:
        return True
