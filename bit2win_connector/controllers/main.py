import requests
import json
# from localStoragePy import localStoragePy

from odoo import models
from odoo import http, _, exceptions
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

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
        result = ''
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
                token_result = content.text
                # local_storage = localStoragePy('bit2win', 'sqlite')
                # local_storage.setItem('b2w-access-token', token_result)
                # result = local_storage.getItem('b2w-access-token')
        except Exception as e:
            return str({'status': 404, 'message': 'Register Error'})
        return str({'status': 200, 'result': result, 'message': 'Registration token saved successfully'})

    @http.route('/say_hello', auth="public", csrf=False, type='http', cors="*")
    def hello(self):
        return str({'status': 200, 'message': 'Hello API APP'})
