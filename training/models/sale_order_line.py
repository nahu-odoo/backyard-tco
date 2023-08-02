from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    min_age = fields.Integer("Minimum Age", related="product_id.min_age")
