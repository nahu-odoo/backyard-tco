from odoo import fields, models

class Sale(models.Model):
    _inherit = "sale.order"

    expense_level = fields.Selection([('cheap', 'Cheap'), ('normal', 'Normal'), ('expensive', 'Expensive')])
