import datetime
from odoo import http
from odoo.http import request
import json

class Controllers(http.Controller):

    # @http.route('/hello')
    # def hello(self, **kw):
    #     return "Hello, world!"

    @http.route(['/hello', '/hello/<string:name>'])
    def hello(self, name="world", **kw):
        return "Hello, %s!" % name

    @http.route(['/json_data'], auth='public')
    def json_data(self, **kw):
        headers = {'Content-Type': 'application/json'}
        data = {'a': 1, 'b': 2}

        return request.make_response(json.dumps(data), headers=headers)

    @http.route(['/total', '/total/<string:date>'])
    def total_sale(self, date=None, **kw):
        if date:
            date_data = datetime.datetime.strptime(date, '%Y-%m-%d')
            total = request.env['sale.order'].search_count([('create_date', '=', date_data)])
        else:
            total = request.env['sale.order'].search_count([])
        return "Total Sale: %s" % total
