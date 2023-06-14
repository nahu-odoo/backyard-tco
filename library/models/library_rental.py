from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class Rental(models.Model):
    _name = "library.rental"

    # user = fields.Char()
    user_id = fields.Many2one('res.partner')
    # book = fields.Char()
    book = fields.Many2one("library.book", required=True)
    date = fields.Date()
    due_date = fields.Date()
    overdue_fine = fields.Float(compute="_compute_overdue_fine")
    state = fields.Selection([('borrow', 'Borrowed'), ('returned', 'Returned')], default="borrow")

    @api.depends('overdue_fine')
    def _compute_overdue_fine(self):
        today = fields.Date.today()
        for rec in self:
            if rec.due_date and rec.due_date < today:
                rec.overdue_fine = (today - rec.due_date).days * 10
            else:
                rec.overdue_fine = 0

    @api.model
    def create(self, vals):
        vals['date'] = fields.Date.today()
        vals['due_date'] = fields.Date.today() + relativedelta(months=1)
        return super().create(vals)

    def search_rentals(self):
        today = fields.Date.today()
        return self.search([('due_date', '>', today)], order='due_date desc')

    def return_book(self):
        self.state = 'returned'

    @api.depends('user_id', 'book')
    def _compute_display_name(self):
        for rental in self:
            rental.display_name = '%s - %s' % (rental.user_id.name, rental.book.name)
