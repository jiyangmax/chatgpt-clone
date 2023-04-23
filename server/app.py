from flask import Flask
from server.website import Website
from server.backend import Backend_Api
from server.errors  import *


app = Flask(__name__, template_folder='./../client/html')

site = Website(app)
for route in site.routes:
    app.add_url_rule(
        route,
        view_func = site.routes[route]['function'],
        methods   = site.routes[route]['methods'],
    )

backend_api  = Backend_Api(app)
for route in backend_api.routes:
        app.add_url_rule(
            route,
            view_func = backend_api.routes[route]['function'],
            methods   = backend_api.routes[route]['methods'],
        )