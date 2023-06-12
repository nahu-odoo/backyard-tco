from odoo import fields, models

class Rental(models.Model):
    _name = "library.rental"

    user = fields.Char()
    # book = fields.Char()
    book = fields.Many2one("library.book")
    date = fields.Date()
