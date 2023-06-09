import logging
import os
import json

from flask import Flask
from flask import request, Response


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

PROXY_URL = os.environ.get('PROXY_URL')

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def _proxy(*args, **kwargs):

    app.logger.info(f"Returning #{request.url}")
    method=request.method
    headers = {key: value for (key, value) in request.headers}
    data=request.get_data()
    request.cookies

    response = Response(json.dumps(headers), 200, headers)

    return response


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=5005, debug=True)
# [END gae_python37_app]
