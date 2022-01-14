import requests
import json
from odoo import models
from odoo import http, _, exceptions
from odoo.http import request
# import logging
# _logger = logging.getLogger(__name__)

# values request
client_id = 'client-internal-test-03'
client_secret = '72a3be54-cc49-46f3-9e4f-8b4302905162'
grant_type = 'password'
password = 'test'
username = 'test'
url_web = 'https://login-test.bit2win.cloud/auth/realms/internal-test-03/protocol/openid-connect/token'


class User(http.Controller):

    # /api/user/register
    @http.route('/api/user/register', auth="public", csrf=False, type='http', cors="*")
    def push_register(self, **kw):
        try:
            data_register = {
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': grant_type,
                'password': password,
                'username': username,
                'url': url_web
            }
            content = requests.post(url_web, data=data_register)
            if content:
                token_result = json.loads(content.text)['access_token']
        except Exception as e:
            return json.dumps({'status': 404, 'message': 'Register Error'}, sort_keys=False)
        return json.dumps({'status': 200, 'result': token_result, 'message': 'Request token successfully'}, sort_keys=False)

    @http.route('/say_hello', auth="public", csrf=False, type='http', cors="*")
    def hello(self):
        return json.dumps({'status': 200, 'message': 'Hello API Bit2win'}, sort_keys=False)
