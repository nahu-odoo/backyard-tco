from odoo import fields, models

class Rental(models.Model):
    _name = "library.rental"

    # user = fields.Char()
    user_id = fields.Many2one('res.partner')
    # book = fields.Char()
    book = fields.Many2one("library.book")
    date = fields.Date()
