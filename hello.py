def app(environ, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  qstr = environ['QUERY_STRING']
  body = qstr.replace('&', '\n')
  start_response(status, headers)
  return body
