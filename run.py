from gevent.wsgi import WSGIServer
from server import app
import config
from info import MyDict, classify2
import info

info.setup()
http_server = WSGIServer(('', config.PORT), app)
http_server.serve_forever()