def mock_api(path, file_path):
    from httmock import urlmatch, response
    @urlmatch(scheme = 'https', netloc = 'api.webpay.jp', path = '/v1' + path)
    def webpay_api_mock(url, request):
        from os import path
        dump = path.dirname(path.abspath(__file__)) + '/mock/' + file_path
        file = open(dump)
        lines = file.readlines()
        file.close

        status = 0
        headers = {}
        body = ''
        body_started = False

        for i in range(len(lines)):
            line = lines[i]
            if i == 0:
                status = int(line.split(' ')[1])
            elif body_started:
                body += line
            elif (line.strip() == ''):
                body_started = True
            else:
                key, value = line.split(':', 1)
                headers[key] = value.strip()

        return response(status, content = body.encode('utf-8'), headers = headers, request = request)
    return webpay_api_mock
