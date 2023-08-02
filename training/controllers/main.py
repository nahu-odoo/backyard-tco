# -*- coding: utf-8 -*-
import datetime
from odoo import http, SUPERUSER_ID
from odoo.http import request
import json

class Controllers(http.Controller):

    @http.route('/hello', auth='public')
    def hello(self, **kw):
        return "Hello, World!"

    @http.route(['/hello', '/hello/<string:name>'])
    def hello(self, name="world", **kw):
        return "Hello, %s!" % name

    @http.route('/hello_json')
    def hello_json(self, **kw):
        return json.dumps({"data": "Hello, World!"})

    @http.route("/sale_total")
    def sale_total(self, date=None, **kw):
        if request.httprequest.method == "POST":
            return request.redirect('/total/' + date)
        sales = request.env['sale.order'].search([])
        return "%s" % sum(sales.mapped('amount_total'))

    @http.route("/total/<string:date>")
    def sale_total_at_date(self, date, **kw):
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        sales = request.env['sale.order'].search([('date_order', '<=', parsed_date)])
        return "%s" % sum(sales.mapped('amount_total'))

    @http.route('/index')
    def index(self, **kw):
        return request.render("training.total_amount")

    @http.route('/test', type='http', auth='public')
    def test(self, **kwargs):
        data = "test"
        return request.make_response(data)

    @http.route("/json_data", auth='none')
    def json_data(self, **values):
        headers = {'Content-Type': 'application/json'}
        body = {'x': 1, 'y': 2}

        return request.make_response(json.dumps(body), headers)

    @http.route("/start")
    def start(self, **kw):
        vals = {'name': 'test', 'age': 20}
        return request.render("training.example_template", vals)

    @http.route("/sale/<int:sale_id>")
    def sale(self, sale_id, **kw):
        sale = request.env['sale.order'].browse(sale_id)
        return request.render("training.sale_web", {'order': sale})
