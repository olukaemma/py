__author__ = 'olukaemma'
def test_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello, world!\n'

test_app()