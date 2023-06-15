import datetime
from odoo import http, api, SUPERUSER_ID
from odoo.http import request
import json

class Controllers(http.Controller):

    @http.route('/books', auth='public')
    def books(self, **kw):
        books = request.env['library.book'].sudo().search([])
        values = {"books": books}
        return request.render('library.template_book', values)

    @http.route('/late')
    def late(self, **kw):
        late_rent = request.env['library.rental'].sudo().search([('due_date', '<', datetime.date.today())])
        headers = {"Content-Type": "application/json"}

        users = late_rent.user_id
        data = {}
        for user in users:
            rents = late_rent.filtered(lambda r: r.user_id == user)
            data[user.name] = [{'book': r.book.name, 'overdue': r.overdue_fine} for r in rents]

        return request.make_response(json.dumps(data), headers=headers)
