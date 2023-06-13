from odoo import fields, models

class Book(models.Model):
    _name = "library.book"

    name = fields.Char("Title", required=True)
    # author = fields.Char()
    authors = fields.Many2many("res.partner")
    isbn = fields.Char()
    summary = fields.Text()
