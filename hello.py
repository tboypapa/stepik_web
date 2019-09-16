def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['\r\n'.join(env['QUERY_STRING'].split('&'))]
