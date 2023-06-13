from odoo import fields, models

class Magazine(models.Model):
    _name = "library.magazine"
    _inherit = "library.book"

    issue_date = fields.Date()
